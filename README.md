# Greenacre website — local preview & editing

This branch (refactor/paths-and-pages) contains small infrastructure changes to make previewing and working on the site smoother.

What I changed in this branch so far
- Added assets/dynamic-base.js — a tiny script that inserts a <base href="/.../"> when pages are served from username.github.io so root-absolute links work on the GitHub Pages repo subpath. It does nothing on a custom domain.
- Copied existing backups into the archive/ folder (index.html.bak and our-school/campus-facilities/index.html.bak).

Why this helps
- When you preview the site at https://<username>.github.io/<repo>/ the browser will resolve "/..." URLs to the right subpath so pages and assets work properly while we keep root-absolute links for the eventual custom domain.
- The dynamic helper is reversible and has no visual impact.

Local preview instructions
1. git clone git@github.com:GreenacreAdmin/greenacre-website-draft.git
2. cd greenacre-website-draft
3. git fetch origin
4. git checkout refactor/paths-and-pages
5. python -m http.server 8000
6. Open http://localhost:8000/index.html to preview locally (note: the dynamic-base only runs when hostname ends with .github.io — local preview verifies markup and styling)

How I will proceed next (with your approval)
- Insert a small inline <script> that loads assets/dynamic-base.js into the <head> of every HTML page so the helper runs in the browser on each page load. I will add the script tag as the first child of <head> (safe, low risk).
- Archive or remove backup files (I copied them to archive/; tell me if you want originals removed).
- (Optional) Run lossless image compression on large images and team photos (I will only run lossless compression unless you ask for stronger lossy compression). If you prefer I can skip the images.

If you want to preview the branch on GitHub Pages you can temporarily set the repository Pages to the branch refactor/paths-and-pages (Settings → Pages) or review the changes in this branch and merge when ready.

Next step? Reply with one of:
- `inject-base-to-all` — I will insert the <script src="/assets/dynamic-base.js"></script> into the <head> of every HTML page on this branch and push the edits (then open a PR for you to review).
- `skip-inject` — do not inject; keep the helper file only.
- `compress-images` — I will run lossless image optimizations on selected images and push them (I will list which images beforehand).
