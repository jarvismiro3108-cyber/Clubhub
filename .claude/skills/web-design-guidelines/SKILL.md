---
name: web-design-guidelines
description: Audit Club Hub's UI code against Vercel's Web Interface Guidelines (accessibility, focus, forms, motion, typography, performance, i18n). Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or before shipping a front-end change.
argument-hint: <file-or-pattern, default src/template.html>
---

# Web Interface Guidelines audit

Reviews front-end code against the rules in Vercel's Web Interface Guidelines
(https://vercel.com/design/guidelines, rules file MIT-licensed by Vercel Labs).
This is Club Hub's own short wrapper; the rules themselves are always fetched fresh.

## Steps

1. Fetch the current rules (plain Bash works in Club Hub's cloud sessions; WebFetch is the fallback):

   ```
   curl -sSf https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
   ```

   If both fail, say so and stop. Do not audit from memory.
2. Read the files to review. With no argument, review `src/template.html` (the whole front end: HTML, CSS and JS)
   and `worker.js` only for anything it renders. Never review or edit `public/index.html`; it is built from the template.
3. Check every rule in the fetched file. Rules written for React (`onClick`, `<Link>`, hooks) apply to their plain-DOM
   equivalents here: the template builds DOM with the `el()` helper, so look at the attributes and listeners it sets.
4. Report findings in the format the fetched rules ask for (`file:line` plus the issue), grouped by severity, most
   important first. Skip rules that cannot apply to a single-file vanilla site and say which ones you skipped.
5. Only change code when the user asks for fixes. After fixing, run `python3 build.py` and check the pages in
   Playwright at phone (390px) and desktop (1280px) widths, light and dark.
