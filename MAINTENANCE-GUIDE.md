# Greenacre Website Maintenance Guide

This guide covers routine content and layout maintenance for the Greenacre website. The site is maintained as static HTML, CSS and JavaScript. Routine changes do not require a framework, build process or dependency installation.

Use `STYLE-INDEX.md` to choose an existing design pattern. Use `STYLE-MAP.md` to locate the HTML and CSS that control it.

## 1. Safe working process

1. Work only in the confirmed Greenacre repository.
2. Confirm the current branch, commit and working-tree state before editing:

   ```sh
   git branch --show-current
   git rev-parse --short HEAD
   git status --short
   ```

3. Inspect the existing component and every CSS rule that affects it before making a change. Later page-level or `stage` rules may override earlier rules.
4. Make the smallest change that satisfies the requirement. Do not reformat or rewrite unrelated working markup.
5. Use British English in website copy. Do not use em dashes.
6. Review the change at desktop, tablet and true-mobile widths.
7. Check the diff before committing:

   ```sh
   git diff --check
   git diff
   ```

8. Commit one approved task at a time. Push to `main` only after approval.
9. Inspect the deployed GitHub Pages site before beginning the next task.

The recovery tag `known-good-baseline-2026-09-03` must be preserved.

## 2. Reusing an existing section

When adding a section that should match another section:

1. Find the closest existing section in the rendered site and its source file.
2. Copy only that section's semantic HTML structure.
3. Reuse its existing classes. Do not duplicate the CSS under a new class name unless the new section genuinely needs different behaviour.
4. Replace headings, copy, links, image paths and accessible labels.
5. Keep heading order logical. A normal page should have one `h1`, followed by `h2` section headings and `h3` subsections where needed.
6. Check the sections immediately before and after the new section. Preserve the established green, cream, white and accent colour rhythm.
7. Test text wrapping, grid collapse, image cropping and spacing at all three responsive ranges.

The homepage has bespoke styles in `index.html`. Internal pages should prefer the shared patterns documented in `STYLE-INDEX.md`.

## 3. Removing or moving a section

Before removing a section, check for:

- navigation or in-page links pointing to its `id`
- JavaScript selectors that reference its classes or elements
- content that does not exist on another appropriate page
- a background transition that will change when two formerly separated sections become adjacent

Remove only the section and references that become invalid. Do not remove shared CSS merely because one instance has gone. Confirm that the selector is unused across the whole repository first.

When moving a section, preserve its complete component markup and any accessibility attributes. Recheck cascade order because page-level selectors can depend on document position.

## 4. Adding a staff member

The staff roster is in `our-school/our-team/index.html`. Original staff photographs are in `assets/images/team/`; the page now serves smaller WebP copies from `assets/images/optimized/`.

Add the new person to the appropriate `.team-grid-v2` using the existing card structure:

```html
<article class="team-person-v2">
  <div class="team-avatar-v2">
    <img
      src="../../assets/images/optimized/team-example-name.webp"
      alt="Ms. Example Name"
      loading="lazy"
      decoding="async"
    />
  </div>
  <div class="team-copy-v2">
    <h4>Ms. Example Name</h4>
    <p>Role title</p>
  </div>
</article>
```

Use the person's agreed display name and role. Keep titles and capitalisation consistent with neighbouring cards. If no role is shown for others in that group, follow the existing group pattern.

## 5. Removing or updating a staff member

To remove a staff member:

1. Remove only that person's `.team-person-v2` article.
2. Confirm that the remaining grid closes correctly and no empty category remains.
3. Remove the photograph only after confirming that no other page references it:

   ```sh
   rg "image-file-name" .
   ```

To change a name or role, update the visible text and the image `alt` text where appropriate. Do not rename the image unless there is a clear maintenance benefit, since renaming also requires updating every reference.

## 6. Staff photograph standard

Original staff photographs use square PNG files, normally `570 × 570` pixels, with transparent backgrounds. Match that established format when preparing a replacement, then export a WebP copy for the website, preserving dimensions and transparency.

- Use a square crop with the face positioned consistently with neighbouring portraits.
- Keep the transparent background and existing visual treatment.
- Use a concise, lowercase filename. Use hyphens where needed, for example `eh-nyaw.png`.
- Do not stretch a portrait or change its aspect ratio in HTML.
- Optimise the file without visibly reducing quality.
- Keep the `<img>` attributes `loading="lazy"` and `decoding="async"`.
- Set useful alternative text to the staff member's displayed name.

For a straightforward replacement, update both the original and its corresponding served WebP copy. Updating only the original PNG will not change the visible portrait. Retaining the served filename avoids changing the HTML, but use a cache-busting version when checking a replacement. After replacement, check the portrait on a normal desktop display and a real or accurately emulated mobile display.

The homepage hero also uses an optimised WebP copy. Existing efficient WebP photos in `current-site/` and `homepage-embedded/` remain in use. Original files are retained for future editing; logos are not part of photo optimisation.

Ordinary content photography is standardised by `assets/current-school-photos.css`. These frames use a responsive 3:2 ratio with `object-fit: cover`; source images do not need to share that ratio. The homepage is deliberately separate. The Head of School portrait and the full-width swimming-pool image are intentional composition-led exceptions. When adding a normal content photo, reuse `.current-school-photo` rather than introducing a page-specific height or aspect ratio. If the shared photo stylesheet changes, update its cache-version query consistently on every page that loads it.

Staff groups use native HTML accordions (`details.staff-disclosure`), styled by `assets/team-accordion.css`. Leadership has the `open` attribute by default. Keep each group's stable ID so saved direct links still work. Edit its title inside `summary > h3` and its staff cards inside `.staff-panel .team-grid-v2`. `assets/team-accordion.js` supplies Expand all / Collapse all and opens groups reached by a direct link. Individual groups still work without JavaScript. There are no staff-count labels to maintain.

## 7. Links and GitHub Pages paths

The draft site is deployed under `/greenacre-website-draft/`, not at the GitHub account root. A bare root link such as `href="/"` can therefore be wrong on GitHub Pages.

Existing internal navigation uses `data-path` attributes with `assets/site-routing-mobile-nav.js` to account for the deployment base. When maintaining an existing navigation link, preserve its `data-path` attribute and follow the established pattern.

For ordinary content links:

- inspect how equivalent links work from both the homepage and nested pages
- avoid device-specific or JavaScript-only fixes
- verify the link from the GitHub Pages deployment, not only a local preview
- ensure the approach remains sensible when the site later moves to its live domain

External links should use a complete `https://` URL. Links opening a new tab should retain `rel="noopener noreferrer"`.

## 8. Shared headers, navigation and footers

Header and navigation ownership is documented in `STYLE-INDEX.md`. In particular:

- `assets/site-header-styles.css` owns the base header and mobile layout
- `assets/stage16-standard-navigation.css` owns desktop dropdown behaviour
- `assets/stage25-header-uniform.css` enforces the final compact header dimensions
- `assets/site-routing-mobile-nav.js` controls deployment-aware navigation and mobile state

Do not create another navigation implementation or change header height while making a text-only adjustment.

Footer styling belongs in `assets/site-footer.css`. Do not introduce page-specific footer styling. Check accreditation logos, school details and the homepage link after any footer edit.

## 9. Responsive verification

Treat desktop, tablet and true mobile as separate layouts.

At minimum, verify:

- desktop navigation fits without wrapping or collision above the `981px` breakpoint
- dropdowns remain aligned and usable with mouse and keyboard
- the tablet menu opens, closes and identifies the current section correctly
- the true-mobile menu, typography and card grids do not overlap
- images remain correctly cropped and do not distort
- fixed footer content does not obscure page content
- focus states and link targets still work

Narrowing a desktop browser is useful, but it does not replace checking a real phone for routing, viewport and touch behaviour.

## 10. Final checks for routine updates

Before requesting approval, confirm:

- only intended files changed
- no placeholder text or abbreviated source was introduced
- headings and British English copy are correct
- all edited image and link paths resolve
- desktop, tablet and mobile layouts were checked
- unrelated pages did not inherit a shared-style regression
- `git diff --check` reports no whitespace errors
- the complete diff is small enough to review confidently

After deployment, inspect the actual GitHub Pages URL and the affected nested page before considering the update complete.
