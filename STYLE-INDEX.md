# Greenacre Website Style Index

Reference for maintaining and extending the Greenacre website.

Before creating a new component, inspect the current source and reuse an existing pattern wherever appropriate.

## 1. Typography

Primary shared file:
`assets/site-typography.css`

Typography hierarchy:
- `h1` - page title
- `h2` - section title
- `h3` - subsection title
- `h4` - component/card title
- `p` - normal body copy
- `.lead` - introductory emphasis
- `.supporting-text` - secondary supporting copy
- `.caption-text` - captions/small explanatory text

Fonts currently used:
- Comfortaa - principal website typeface
- Bree Serif - selected identity/footer use
- Roboto - selected footer-detail use

Related safeguards:
`assets/formatting-safeguards.css`

Do not introduce page-specific typography unless an existing hierarchy genuinely cannot express the content.

## 2. Header and navigation

Files:
- `assets/site-header-styles.css`
- `assets/stage16-standard-navigation.css`
- `assets/stage25-header-uniform.css`
- `assets/site-routing-mobile-nav.js`

Core classes:
- `.site-header`
- `.site-header__inner`
- `.site-brand`
- `.site-nav`
- `.nav-drop`
- `.nav-menu`
- `.menu-toggle`
- `.nav-section-current`
- `[aria-current="page"]`

Behaviour:
- 981px and above: desktop hover/focus dropdowns
- 980px and below: Menu button with accordion section headings
- Home and Contact are direct links
- exact page receives `aria-current="page"`
- current parent section receives `.nav-section-current`

Important ownership:
`site-header-styles.css` contains the base header appearance and mobile layout.

`stage16-standard-navigation.css` contains the desktop dropdown visibility/transition behaviour.

`stage25-header-uniform.css` is an override layer which deliberately forces the final compact header/logo dimensions. Its dimensions override earlier values in `site-header-styles.css`.

Do not create a second navigation implementation.

## 3. Heroes and section headings

Primary file:
`assets/site-hero.css`

Common classes:
- `.page-hero`
- `.hero`
- `.hero-copy`
- `.eyebrow`
- `.kicker`

Use `.page-hero` for normal internal-page introductions.

The homepage hero is bespoke and remains primarily defined in `index.html`.

## 4. Core layout

Primary shared file:
`assets/site-components.css`

Reusable layout:
- `.wrap` - normal content width, though some page-local definitions remain
- `.grid2` - standard two-column layout
- `.grid2.reverse` - reversed two-column proportions
- `.cards` - standard three-column card grid, collapsing on smaller screens

Prefer these before creating a new generic grid.

## 5. Shared card appearance

The website has several semantic card types whose base structures often originate in page-local CSS.

Their common visual family is imposed principally by:
`assets/formatting-safeguards.css`

The shared card selector includes:
- `.cards > .card`
- `.feature-list > .feature`
- `.info-grid > .info-card`
- `.info-card-grid > .info-card`
- `.service-list > .service`
- `.seven-grid > .seven-card`

This shared layer creates the common treatment:
- white background
- Greenacre border/accent
- rounded corners
- consistent shadow
- common visual relationship between otherwise different card types

Semantic card families include:
- `.card` - ordinary contained content
- `.feature` - short highlighted concept
- `.info-card` - factual/information content
- `.service` - service information
- `.seven-card` - Early Years learning-area card
- `.note`
- `.notice`
- `.step`
- `.resource-card`

Do not assume all these classes are defined in `site-components.css`. Many originate in page-local CSS and receive common appearance through `formatting-safeguards.css`.

Before creating a new card, choose an existing semantic type where possible.

## 6. Buttons and links

Primary shared file:
`assets/site-components.css`

Component-style links:
- `.action`
- `.button`
- `.btn`
- `.phase-link`

Specialist link types:
- `.policy-link`
- `.bullet-links`

Ordinary links inside body content receive the shared Greenacre inline-link rule from `site-components.css`.

Navigation and footer links have their own component styling and should not inherit ordinary body-link appearance.

## 7. Keyboard focus

Primary file:
`assets/site-components.css`

Global interactive controls use `:focus-visible`.

The main `.site-brand` logo deliberately has its own quieter focus treatment.

Preserve that distinction.

## 8. Photography and media

Shared files:
- `assets/site-components.css`
- `assets/stage11-photo-system.css`

`site-components.css` controls the reusable `.photo` container and standard image geometry.

`stage11-photo-system.css` primarily controls the development photography system:
- temporary blur treatment
- replacement stamps
- review markers

Page-specific classes such as `.photo-plan`, `.temp-photo` and specialist image compositions may provide their own dimensions and layouts.

Therefore `stage11-photo-system.css` should not be treated as the owner of all website photography.

Special media:
- `.dofe-video` - embedded Duke of Edinburgh video

When final photographs arrive, preserve the established section composition unless there is a genuine layout problem.

## 9. Footer

Primary file:
`assets/site-footer.css`

Classes:
- `.site-footer`
- `.site-footer__inner`
- `.site-footer__identity`
- `.site-footer__name`
- `.site-footer__details`
- `.site-footer__logos`
- `.site-footer__logo`

`assets/stage11-footer-lock.css` is an older override layer and is currently exceptional rather than the main footer definition.

Do not add page-specific footer styling.

## 10. Tables and structured information

Common classes:
- `.time-table`
- `.info-table`
- `.table-wrap`

Use tables only for genuinely tabular data.

Existing responsive behaviour should be preserved rather than recreating tables with generic layout containers.

## 11. Dark and pale section treatments

Current palette:
- cream/off-white base
- white contained panels
- pale green secondary sections
- dark Greenacre green for occasional high-contrast sections
- orange as a restrained accent

Dark backgrounds should be applied selectively to improve page rhythm, especially where a substantial section currently sits between pale sections.

Do not alternate colours mechanically.

## 12. Homepage components

Primary file:
`index.html`

The homepage contains extensive bespoke CSS including:
- main hero
- quick cards
- welcome composition
- testimonials
- homepage photography
- dark-green sections
- location/social panels

These are homepage-specific unless a component is deliberately promoted into shared CSS.

## 13. Our Team

Primary file:
`our-school/our-team/index.html`

Current active component family:
- `.team-person-v2`
- `.team-avatar-v2`
- `.team-copy-v2`
- `.team-grid-v2`
- `.team-section-v2`
- `.team-heading-v2`

Older Team-related classes remain in the source history/style layers, including several `stageXX` names.

Do not reuse those older variants without checking whether they remain active.

## 14. Clubs & ECAs

Primary file:
`learning/clubs-ecas/index.html`

Specialist components include:
- `.dofe-card-stage42`
- `.dofe-card-copy-stage42`
- `.dofe-video`
- `.timing-card-stage42`
- `.timing-grid-stage42`
- `.clubs-intro-grid-stage42`
- `.clubs-photo-stage42`

These should remain specialist ECA components unless another page genuinely needs the same composition.

## 15. Campus & Facilities

Primary file:
`our-school/campus-facilities/index.html`

Specialist components include:
- `.facility-card-stage24`
- `.facility-grid-stage24`
- `.campus-visit-grid-stage46`
- `.campus-visit-photo-stage46`
- `.visit-campus-photo-stage44`
- `.pool-specific-photo`

## 16. Secondary Parent Information

Primary file:
`parent-information/secondary-parent-information/index.html`

Specialist family:
- `.secondary-parent-info`
- `.secondary-parent-info-hero`
- `.secondary-parent-info-title`
- section-jump navigation
- dense information/card structures

Keep this page's information architecture separate from ordinary content pages.

## 17. Early Years

Specialist components:
- `.seven-grid`
- `.seven-card`

These represent the seven Early Years learning areas.

The card receives part of its shared visual treatment from `formatting-safeguards.css`.

## 18. Design-variety layer

File:
`assets/stage48-design-variety.css`

This is not a general global stylesheet.

It contains later composition refinements for selected pages, particularly:
- Environmentality
- Early Years
- Primary
- Secondary

It includes contained white-panel compositions, alternative section arrangements and specialist responsive treatments.

If a pattern from this file becomes genuinely site-wide, promote it deliberately into a semantically named shared component rather than simply loading this entire file everywhere.

## 19. Historical stage names

Classes/files containing names such as:
- `stage11`
- `stage16`
- `stage24`
- `stage25`
- `stage28`
- `stage42`
- `stage44`
- `stage46`
- `stage48`

describe the development history rather than semantic purpose.

They may still be active and should not be renamed casually.

New reusable components should use semantic names.

## 20. Page-local CSS

Significant page-local CSS still exists, particularly on:
- homepage
- Our Team
- Clubs & ECAs
- Secondary Parent Information
- Campus & Facilities

This is not itself a defect.

Do not refactor working CSS purely for tidiness.

Promote a local component into shared CSS only when it becomes genuinely reusable across multiple pages.

## 21. Adding a new element

Before adding anything new:

1. Identify the content type.
2. Check this index for an existing semantic component.
3. Inspect the exact current HTML and CSS.
4. Reuse the established component where possible.
5. Extend an existing component if only a small variation is required.
6. Create a new component only when the existing system cannot express the content appropriately.
7. Give new classes semantic names, not development-stage names.
8. Update this index when a genuinely reusable component is introduced.

The goal is controlled evolution of the established site rather than continued redesign.

## 22. Exhaustive technical component map

See `STYLE-MAP.md` for the repository-wide technical map of every class currently used in HTML, where it is used, where its CSS is defined, JavaScript-controlled states, multi-file definitions and possible legacy/orphan selectors.

`STYLE-INDEX.md` explains the design system semantically. `STYLE-MAP.md` provides the exact technical lookup.

