// Club Hub on Cloudflare: serves the website (public/) and the AI endpoint (/api/*).
// The Gemini key lives in this Worker's settings as the secret GEMINI_API_KEY; it never goes to the browser.
// Optional text variable MODEL picks the Gemini model.

const MAX_PROMPT = 16000;
const PER_IP_PER_MINUTE = 6;
const hits = new Map();
const MODELS = ['gemini-flash-latest', 'gemini-2.5-flash', 'gemini-2.0-flash', 'gemini-flash-lite-latest'];
let goodModel = null;

const CORS = { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET, POST, OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type' };
const json = (status, obj) => new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store', ...CORS } });

async function gemini(env, model, prompt, search) {
  const body = { contents: [{ role: 'user', parts: [{ text: prompt }] }], generationConfig: { temperature: 0.9 } };
  if (search) body.tools = [{ google_search: {} }];
  else body.generationConfig.responseMimeType = 'application/json';
  const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, {
    method: 'POST', headers: { 'Content-Type': 'application/json', 'x-goog-api-key': env.GEMINI_API_KEY }, body: JSON.stringify(body),
  });
  const text = await r.text();
  let data = null; try { data = JSON.parse(text); } catch {}
  return { status: r.status, ok: r.ok, data, raw: text };
}

function extract(data) {
  const cand = data?.candidates?.[0];
  const text = cand?.content?.parts?.map(p => p.text || '').join('') || '';
  const sources = (cand?.groundingMetadata?.groundingChunks || []).map(c => c.web).filter(Boolean)
    .map(w => ({ title: w.title || '', uri: w.uri || '' })).slice(0, 6);
  let result = null;
  try { result = JSON.parse(text); } catch {
    const m = text.match(/\{[\s\S]*\}/); if (m) { try { result = JSON.parse(m[0]); } catch {} }
  }
  return { result, sources };
}

async function ask(env, prompt, search) {
  const list = [...new Set([env.MODEL, goodModel, ...MODELS].filter(Boolean))];
  let last = null;
  for (const model of list) {
    for (const s of search ? [true, false] : [false]) {
      const r = await gemini(env, model, prompt, s);
      if (r.status === 429) return { error: 'rate_limited', status: 429 };
      if (r.status === 400 || r.status === 403) {
        const msg = r.data?.error?.message || '';
        if (/api key|API_KEY|permission/i.test(msg)) return { error: 'bad_key', status: r.status, detail: msg.slice(0, 200) };
      }
      if (r.ok) {
        const { result, sources } = extract(r.data);
        if (result) { goodModel = model; return { result, sources, model, searched: s }; }
        last = { error: 'invalid_json', status: 200 };
        continue;
      }
      last = { error: 'ai_error', status: r.status, model, detail: (r.data?.error?.message || r.raw || '').slice(0, 200) };
      if (r.status === 404) break; // model not available: try the next model
    }
  }
  return last || { error: 'ai_error', status: 500 };
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (!url.pathname.startsWith('/api/')) return env.ASSETS.fetch(request);
    if (request.method === 'OPTIONS') return new Response(null, { headers: CORS });
    if (!env.GEMINI_API_KEY) return json(500, { error: 'no_key', detail: 'Add the secret GEMINI_API_KEY to this Worker.' });

    if (url.pathname === '/api/test') {
      const r = await ask(env, 'Reply with only this JSON: {"ok":true}', false);
      return json(r.result ? 200 : 502, r.result ? { ok: true, model: r.model } : r);
    }
    if (url.pathname !== '/api/analyze' || request.method !== 'POST') return json(404, { error: 'not_found' });

    const ip = request.headers.get('CF-Connecting-IP') || 'x';
    const now = Date.now();
    const list = (hits.get(ip) || []).filter(t => now - t < 60000);
    if (list.length >= PER_IP_PER_MINUTE) return json(429, { error: 'rate_limited' });
    list.push(now); hits.set(ip, list);

    let body; try { body = await request.json(); } catch { return json(400, { error: 'bad_request' }); }
    const prompt = String(body?.prompt || '');
    if (!prompt || prompt.length > MAX_PROMPT) return json(400, { error: 'bad_request' });

    const r = await ask(env, prompt, !!body.search);
    if (!r.result) return json(r.status === 429 ? 429 : 502, r);
    return json(200, r);
  },
};
