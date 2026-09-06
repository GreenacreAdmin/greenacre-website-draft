# Greenacre domain cutover

Prepared domain: https://www.greenacre.ac.th/
Current draft: https://greenacreadmin.github.io/greenacre-website-draft/

The CNAME is deliberately not active while reviewing the draft. Adding it redirects the GitHub Pages draft to the custom domain. The user will handle DNS; Codex handles the repository, GitHub Pages custom-domain setting, search metadata and verification at cutover. DNS and certificate issuance can take time; this is not an instantaneous DNS-only switch.

## DNS values

- www CNAME: greenacreadmin.github.io (no repository path).
- If moving the apex greenacre.ac.th too, the GitHub Pages A records are 185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153. Configure matching GitHub IPv6 records or remove only obsolete website AAAA records if present.
- Preserve mail MX, SPF, DKIM, DMARC and unrelated service records.
- Coordinate domain attachment immediately before the DNS change where possible. GitHub recommends attaching/verifying the domain before DNS points to Pages. If DNS has already changed, attach promptly and verify.

## Codex cutover steps

1. Inspect current branch and working-tree state; do not discard unrelated changes. Confirm the user is ready to switch.
2. Run `python3 scripts/update-search-metadata.py --launch`. This updates every public canonical, the sitemap, robots and 404 assets to the final origin and adds CNAME. The URL-only Secondary parent page stays noindex/nofollow and outside the sitemap; aliases stay outside it.
3. Run `python3 scripts/check-site.py` and review the diff. Commit and push the authorised cutover on main.
4. Inspect GitHub Pages through `gh api repos/GreenacreAdmin/greenacre-website-draft/pages`. Confirm cname is www.greenacre.ac.th; configure it if the branch deployment has not done so. Inspect DNS and Pages certificate status. Enable/enforce HTTPS once the certificate is ready.
5. Verify www and apex (if configured), nested navigation, all three unchanged PDFs, the embedded ECA application, representative legacy redirects and an unknown URL's 404. Recheck the live sitemap and canonical URLs.

## Ongoing maintenance

After adding/removing public pages, run `python3 scripts/update-search-metadata.py` followed by `python3 scripts/check-site.py`.
Original PDFs are preserved byte-for-byte under assets/documents; originals.json records their SHA-256 checksums. Replace only when the school supplies a new original. Do not edit their content, dates, prices or formatting.
The ECA app is maintained elsewhere and remains a live iframe, with a direct external fallback. Do not duplicate or edit its data here.
Known old Google Sites paths are listed in scripts/legacy-routes.json. GitHub Pages has no configurable per-path server redirects, so these are immediate HTML redirects with canonical targets and an explicit fallback link.

Reference: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## Unlisted Secondary resources

Preserve `/academics/secondary-information/` and `/academics/secondary-start-of-year/` through cutover. Each embeds its original Apps Script deployment unchanged. Both remain outside public navigation and the sitemap, with `noindex, nofollow`. The earlier draft path `/parent-information/secondary-parent-information/` redirects to the information page. Include both live embeds in the cutover checks.
