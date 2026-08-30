# Greenacre Website Style Index

This file is the reference for adding, editing or reusing visual elements on the Greenacre website.

The site should be treated as an established design system. Before creating a new component, check this index and reuse an existing pattern where possible.

## 1. Core design foundations

### Typography
Primary file:
- `assets/site-typography.css`

Main families:
- Comfortaa — primary site typeface
- Bree Serif — currently used selectively, especially footer identity
- Roboto — currently used selectively, especially footer details

Related:
- `assets/formatting-safeguards.css`

Use this layer for:
- general text behaviour
- heading consistency
- wrapping safeguards
- global typography rules

Do not create page-specific font rules unless there is a clear visual reason.

---

## 2. Header and navigation

Primary files:
- `assets/site-header-styles.css`
- `assets/stage16-standard-navigation.css`
- `assets/stage25-header-uniform.css`
- `assets/site-routing-mobile-nav.js`

Main classes:
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
- Desktop: hover/focus dropdown navigation
- Mobile/tablet: Menu button plus expandable section headings
- Home and Contact remain direct links
- Current exact page uses `aria-current="page"`
- Current section receives `.nav-section-current`

Breakpoint:
- Mobile/tablet navigation ends at 980px
- Desktop navigation begins at 981px

Do not introduce a second navigation system.

---

## 3. Page heroes

Primary file:
- `assets/site-hero.css`

Main classes:
- `.page-hero`
- `.hero`
- `.hero-copy`
- `.eyebrow`
- `.kicker`

Use:
- `.page-hero` for standard internal-page introductions
- `.eyebrow` or `.kicker` for small section labels above headings

The homepage hero is substantially page-specific and remains in `index.html`.

Do not copy homepage hero CSS into internal pages.

---

## 4. General layout

Common classes:
- `.wrap`
- `.grid2`
- `.reverse`
- `.intro-grid`
- `.identity-grid`

Purpose:
- `.wrap` controls normal content width
- `.grid2` is the standard two-column content pattern
- `.reverse` reverses visual order where supported
- specialist grids should be used only when their existing component requires them

Before creating a new grid, check whether `.grid2` or an existing component grid already solves the layout.

---

## 5. Standard cards and contained content

Primary shared file:
- `assets/site-components.css`

General reusable families:
- `.card`
- `.cards`
- `.info-card`
- `.info-grid`
- `.feature`
- `.feature-list`
- `.note`
- `.notice`
- `.step`
- `.steps`
- `.resource-card`
- `.service`
- `.service-list`

### Standard card
Use `.card` for ordinary contained information where no specialist layout is required.

### Information card
Use `.info-card` for compact factual/information content.

### Feature
Use `.feature` for short highlighted concepts within a feature list.

### Note
Use `.note` for contained supporting information.

### Notice
Use `.notice` for information requiring stronger attention, usually with an accent edge.

### Steps
Use `.step` / `.steps` for sequential processes.

Avoid inventing another generic card class unless none of these patterns fits.

---

## 6. Buttons and links

Primary shared file:
- `assets/site-components.css`

Main classes:
- `.action`
- `.button`
- `.btn`
- `.phase-link`

Other specialist link classes:
- `.policy-link`
- `.bullet-links`

Ordinary inline links inside body content use the shared Greenacre inline-link treatment.

Rules:
- Use a button class only for action-like links
- Use ordinary inline links inside prose
- Do not manually apply browser-blue link colours
- Do not add inline colour styles where a shared link style exists

---

## 7. Photography and media

Primary file:
- `assets/stage11-photo-system.css`

Common classes:
- `.photo`
- `.photo-plan`
- `.temp-photo`
- `.photo-blur-layer`
- `.photo-stamp`
- `.photo-instruction`
- `.stamp`
- `.shot`
- `.review-secondary-photo`

Temporary-photo behaviour is deliberate during development.

When final photography is installed:
- preserve the existing container/layout
- replace the image source/background
- remove temporary stamps/instructions where appropriate
- do not redesign the section merely because the photograph changes

Special media:
- `.dofe-video` — Duke of Edinburgh embedded video

---

## 8. Section background treatments

Current general palette:
- cream / off-white default
- white contained sections/cards
- pale green supporting sections
- dark Greenacre green for selected high-contrast sections
- orange used sparingly as an accent

Dark-green sections should be used selectively to break long sequences of pale sections.

Do not alternate backgrounds mechanically. Use dark green where it improves page rhythm and separates substantial content areas.

A separate site-wide visual-variety audit controls future additions of dark-green sections.

---

## 9. Footer

Primary files:
- `assets/site-footer.css`
- `assets/stage11-footer-lock.css`

Main classes:
- `.site-footer`
- `.site-footer__inner`
- `.site-footer__identity`
- `.site-footer__name`
- `.site-footer__details`
- `.site-footer__logos`
- `.site-footer__logo`

The footer is a shared global component.

`stage11-footer-lock.css` is an older override layer and is currently used by only one page. Treat it as legacy/exception code until deliberately reviewed.

Do not add page-specific footer styling.

---

## 10. Tables and structured information

Main classes:
- `.time-table`
- `.info-table`
- `.table-wrap`

Use tables for genuinely tabular information rather than visual layout.

On mobile, retain responsive wrapping/scroll behaviour already defined by the component.

---

## 11. Page-specific component families

These components are valid but should not automatically be reused elsewhere.

### Homepage
File:
- `index.html`

The homepage contains a large amount of local CSS and several bespoke components, including:
- homepage hero
- quick cards
- testimonials
- homepage photography
- homepage dark-green sections
- homepage social/location panels

Treat these as homepage-specific unless a component is deliberately promoted into shared CSS.

### Our Team
File:
- `our-school/our-team/index.html`

Current active family:
- `.team-person-v2`
- `.team-avatar-v2`
- `.team-copy-v2`
- `.team-grid-v2`
- `.team-section-v2`
- `.team-heading-v2`

Other Team-related names such as:
- `.person-card`
- `.team-card-stage28`
- `.team-group-card-stage44`
- `.team-intro-card-stage44`

may represent older iterations. Do not reuse them without confirming they are still active.

### Clubs & ECAs
File:
- `learning/clubs-ecas/index.html`

Specialist components include:
- `.dofe-card-stage42`
- `.dofe-card-copy-stage42`
- `.dofe-video`
- `.timing-card-stage42`
- `.timing-grid-stage42`
- `.clubs-intro-grid-stage42`
- `.clubs-photo-stage42`

These belong primarily to the Clubs page.

### Campus & Facilities
File:
- `our-school/campus-facilities/index.html`

Specialist components include:
- `.facility-card-stage24`
- `.facility-grid-stage24`
- `.campus-visit-grid-stage46`
- `.campus-visit-photo-stage46`
- `.visit-campus-photo-stage44`
- `.pool-specific-photo`

### Secondary Parent Information
File:
- `parent-information/secondary-parent-information/index.html`

Specialist component family:
- `.secondary-parent-info`
- `.secondary-parent-info-hero`
- `.secondary-parent-info-title`
- section-jump navigation
- page-specific information/card structures

Keep this page's specialist navigation and dense information layout separate from ordinary content pages.

### Early Years
Specialist:
- `.seven-grid`
- `.seven-card`

Use for the seven Early Years learning areas only unless another genuine seven-part framework requires the same treatment.

---

## 12. Shared design-variety layer

File:
- `assets/stage48-design-variety.css`

Currently loaded by only a small number of pages.

It contains later-stage visual-composition refinements rather than core global rules.

Treat this as an enhancement layer, not a universal component library.

If a rule proves useful across many pages, move it deliberately into an appropriately named shared stylesheet rather than simply loading `stage48-design-variety.css` everywhere.

---

## 13. Known maintenance ambiguities

The following should be treated cautiously.

### Historical `stageXX` class/file names
Examples:
- `stage11`
- `stage16`
- `stage24`
- `stage25`
- `stage28`
- `stage42`
- `stage44`
- `stage46`
- `stage48`

These names describe when components were created, not what they do.

They are currently functional but are poor semantic references for future work.

Do not rename them casually because they may be widely connected to existing markup. New components should use semantic names.

### Multiple overlapping card systems
The site contains:
- `.card`
- `.info-card`
- `.note-card`
- `.facility-card-stage24`
- `.timing-card-stage42`
- Team card variants
- other specialist cards

Before creating another card:
1. identify its purpose
2. check the standard shared card families
3. use a specialist card only when the content genuinely requires different behaviour

### Page-local CSS
Several pages still contain substantial local `<style>` blocks.

Major outliers:
- homepage
- Our Team
- Clubs & ECAs
- Secondary Parent Information
- Campus & Facilities

This is not currently a defect. Do not refactor merely for tidiness.

If a local pattern begins appearing on several pages, then promote it into shared CSS.

---

## 14. Rule for adding future elements

Before adding a new visual element:

1. Identify the content type.
2. Check this index for an existing component.
3. Inspect the current source and exact active CSS.
4. Reuse the existing class where suitable.
5. If variation is required, extend the existing component rather than duplicate it.
6. Create a new component only when the existing design system genuinely cannot express the content.
7. Use semantic names for all new classes.
8. Update this index if a genuinely reusable component is added.

The objective is controlled evolution of the existing site, not continued redesign.

---

## 15. Current component hierarchy

Use this order of preference:

**Global foundation**
Typography → layout → shared components → header/navigation → footer → hero

**Reusable content patterns**
Standard card → info card → feature → note/notice → action/button → table

**Specialist components**
Phase-specific, Team, ECA, Campus, Secondary Parent Information and homepage components

**One-off styling**
Only when no reusable or specialist component can reasonably perform the job.
