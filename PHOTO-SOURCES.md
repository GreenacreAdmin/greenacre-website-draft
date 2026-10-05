# Website photo selections

Updated 5 October 2026. Each photograph is used once across the 27 photography-checklist slots. Logos and staff-roster portraits are outside this list.

The selection combines 14 photographs from the supplied ZIP, the separately supplied Head of School portrait and About classroom photograph, 9 retained or reused photographs from the public school site, and the existing homepage hero and Work with Us photograph. The user confirmed the Early Years and Secondary year groups, approved the tighter sand-play crop and mixed selection, and asked to retain the current pool photograph.

## Homepage

| Frame | Source | Served asset |
|---|---|---|
| Hero | Existing approved seedlings image; retained | `assets/images/optimized/home-hero-seedlings-v3.*` |
| intro-photo | `IMG_4518.PNG` | `assets/images/school-2026/individual-support-*.webp`; 50% 35% |
| phase-card.early::before | `IMG_4830.PNG` | `assets/images/school-2026/early-years-nature-*.webp` |
| phase-card.primary::before | [https://www.greenacre.ac.th/](https://www.greenacre.ac.th/) | `assets/images/school-2026/reading-together-*.webp` |
| phase-card.secondary::before | `IMG_5037.PNG` | `assets/images/school-2026/science-practical-*.webp`; 100% 0% |
| identity-photo | User-selected imagegen edit of `IMG_4188.HEIC` | `assets/images/school-2026/watering-together-*.webp` |

## Internal pages

| Page / photo slot | Source | Served asset / crop |
|---|---|---|
| `learning/curriculum/` / 1 | [Current school site](https://www.greenacre.ac.th/academics/curriculum) | `assets/images/current-site/academics-curriculum-02.webp` |
| `learning/curriculum/` / 2 | `IMG_4117.HEIC` | `assets/images/school-2026/primary-art-*.webp`; 50% 100% |
| `learning/early-years/` / 1 | [Current school site](https://www.greenacre.ac.th/academics/early-years-foundation-years) | `assets/images/current-site/academics-early-years-foundation-years-02.webp` |
| `learning/early-years/` / 2 | `IMG_5039.PNG` | `assets/images/school-2026/early-years-sand-*.webp`; 50% 25% |
| `learning/primary/` / 1 | `IMG_5023.PNG` | `assets/images/school-2026/primary-teaching-*.webp`; 50% 15% |
| `learning/primary/` / 2 | [Current school site](https://www.greenacre.ac.th/academics/primary) | `assets/images/current-site/academics-primary-02.webp` |
| `learning/secondary/` / 1 | `IMG_5024.PNG` | `assets/images/school-2026/secondary-maths-*.webp`; 50% 50% |
| `learning/secondary/` / 2 | `IMG_5029.JPG`, enhanced placeholder | `assets/images/school-2026/science-independent-*.webp`; 50% 0% |
| `learning/clubs-ecas/` / 1 | User-supplied `unnamed (2).jpg` | `assets/images/school-2026/table-tennis-*.webp`; 25% 50% |
| `our-school/about-greenacre/` / 1 | Separately supplied `unnamed (1).jpg` | `assets/images/school-2026/about-classroom-*.webp`; 50% 50% |
| `our-school/campus-facilities/` / 1 | User-requested imagegen enhancement of `IMG_4184.HEIC` | `assets/images/school-2026/growing-area-*.webp`; 50% 85% |
| `our-school/campus-facilities/` / 2 | `IMG_4219.PNG` | `assets/images/school-2026/library-reading-*.webp`; 50% 65% |
| `our-school/campus-facilities/` / 3 | User-requested imagegen enhancement of the current school pool photo | `assets/images/school-2026/swimming-pool-*.webp`; centred in the existing wide frame |
| `our-school/environmentality/` / 1 | [Current school site](https://www.greenacre.ac.th/home) | `assets/images/current-site/home-02.webp` |
| `our-school/environmentality/` / 2 | [Current school site](https://www.greenacre.ac.th/academics/environmentality) | `assets/images/current-site/academics-environmentality-03.webp` |
| `our-school/wellbeing/` / 1 | [Current school site](https://www.greenacre.ac.th/extra-curricular/wellbeing) | `assets/images/current-site/extra-curricular-wellbeing-02.webp` |
| `our-school/wellbeing/` / 2 | `IMG_5038.PNG` | `assets/images/school-2026/outdoor-chess-*.webp`; 50% 72% |
| `admissions/admissions-visits/` / 1 | `IMG_4998.PNG` | `assets/images/school-2026/classroom-welcome-*.webp`; 50% 55% |
| `parent-information/services/` / 1 | [Current school site](https://www.greenacre.ac.th/academics/environmentality) | `assets/images/current-site/academics-environmentality-02.webp` |
| `our-school/head-of-school-welcome/` / 1 | `1742964487955 (1).jpg` | `assets/images/school-2026/head-dara-nagle-*.webp`; 50% 0% |
| `work-with-us/` / 1 | Existing teacher-at-desk selection; retained | Existing responsive recruitment photo; bottom-aligned 3:2 crop |

## Crop and delivery notes

- Original ZIP and separate portrait remain outside the deployed repository. New web assets are full-frame WebP derivatives at 480, 960 and up to 1440 pixels wide, with no upscaling. HTML `srcset` and homepage CSS `image-set` serve responsive versions.
- The existing frame sizes, border treatments, spacing and responsive layouts are retained. Individual images use crop positions that keep the main faces and interaction visible.
- The Head of School portrait keeps the previous displayed ratio of 902:1327; it is cropped within that frame.
- Sand play is used only on the Early Years page. The 3:2 crop prioritises both faces and the activity; it cannot retain the whole bowl from the tight original.
- `IMG_5026.JPG` remains a reserve because its portrait composition fits the ordinary landscape frames poorly. The two `IMG_4218` versions are already represented by Work with Us and are not added elsewhere.
- All replacement badges have been removed from the selected photo frames, including intentionally retained images.
- Parent Services retains a produce photograph as a food-related illustration. It is not labelled as dining. A dedicated dining image would still improve specificity.

## Current-site review

Reviewed the live homepage, Early Years, Primary, Curriculum, Environmentality, Wellbeing, Swimming Pool, Services, Community and Head of School Welcome pages on 5 October 2026. Strong reading, collaboration, classroom participation, outdoor learning, meditation, produce and pool images were retained or reassigned.

The current homepage reading image was downloaded through the browser asset export and optimised as `reading-together-*.webp`. Other reused photographs were already stored in `assets/images/current-site/`. The supplied new portrait supersedes the live site’s lectern photograph.

## Verification

- Visual review at browser viewport widths 1440, 768 and 390 pixels.
- No horizontal overflow or missing photo assets across the 13 selected pages.
- Existing ordinary-content and homepage frame dimensions preserved at all three sizes; portrait ratio explicitly preserved.
- Site checker verifies all 49 pages, relative links, fragments, search metadata and original document checksums.
- No push or deployment was performed as part of this local update.

## Colour and compression review — 5 October 2026

- Converted embedded Display P3 originals to sRGB before WebP export; every revised WebP embeds the sRGB profile. Untagged sources are treated as sRGB.
- Watering-together (IMG_4188) now uses the earlier imagegen colour edit, explicitly selected by the user on 5 October 2026. This supersedes the conventional colour-corrected v2 exports; v3 WebP variants preserve the existing homepage frame and crop position.
- Smaller source images receive light output-size unsharp masking (0.6px radius, 60%, threshold 3; 40% at 480px). The Head portrait is already sufficiently detailed for its smaller frame and receives no sharpening. No upscaling was used.
- Chess and sand retain the authentic photographs with conventional sharpening. Their imagegen trials remain unused. Maths now uses the user-approved imagegen revision described below. The watering-together, growing-area and swimming-pool images use imagegen versions requested by the user.
- WebP quality is 80, or 78 for the detail-heavy badminton and growing-area photographs, with method 6 compression. Revised filenames use `-v2` to avoid stale cached versions.
- In the initial conventional-correction pass, across all 48 responsive variants, file weight fell from 4,789,924 to 4,259,834 bytes (11.1%). This is the whole asset set, not a per-page transfer total or measured speed improvement. All 480px variants are below 50 KB; 960px variants are below 143 KB. The largest 1440px variant is 306 KB.
- Homepage cards retain larger desktop sources to avoid softening the tall cover crops. Mobile backgrounds select 480px at 1× or 960px at 2×; internal images retain responsive source selection, lazy loading and asynchronous decoding.
- Original sources and pre-correction exports remain outside the deployed repository. Detailed processing settings and exact output sizes are in `assets/images/school-2026/sources.json`.

Latest watering selection: imagegen master 1404×1120; exports 480px / 46202 bytes, 960px / 123614 bytes, 1404px / 198968 bytes. No further colour changes or generative edits were applied.

Campus update: enhanced growing-area image is first; library image is second. Existing frames and pool photograph are retained. Growing-area exports: 480px / 50834 bytes, 960px / 163608 bytes, 1440px / 292304 bytes.

About Greenacre first image: user-supplied classroom photograph, full source 1280×724, fitted to the existing 3:2 frame. Both faces and writing activity remain visible.

Pool update: user-requested imagegen quality and colour enhancement, retaining the original photographic composition. Existing desktop and mobile frame rules retained. Original WebP retained for provenance. Responsive exports: 480px / 36822 bytes, 960px / 102922 bytes, 1432px / 171040 bytes.

Secondary maths update: user-approved imagegen revision with tidier uniforms, neutral white walls, cleaner whiteboard, 3:2 landscape composition and whiteboard continuing beyond the left edge. Existing page frame retained. Responsive WebP exports: 480px / 17928 bytes, 960px / 55438 bytes, 1536px / 111722 bytes.

Homepage clarity update: imagegen enhancements of the teacher-and-pupil welcome photograph, FS flower activity and Secondary science card. Existing frames, crop positions and Primary photograph retained.

individual-support: 480px / 22046 bytes, 960px / 58452 bytes, 1440px / 96766 bytes
early-years-nature: 480px / 36956 bytes, 960px / 98330 bytes, 1400px / 154032 bytes
science-independent: 480px / 17672 bytes, 960px / 46024 bytes, 1440px / 78192 bytes

FS card refinement supersedes the preceding v3 export: square composition with the children closer together and a slight smile on the boy at right, as requested. 480px / 45548 bytes, 960px / 132396 bytes, 1254px / 191778 bytes.

Secondary homepage card refinement supersedes v3: brighter window daylight, neutral white lab coat and foreground hand moved outside the bottom edge. 480px / 18044 bytes, 960px / 49240 bytes, 1440px / 84130 bytes.

FS homepage card reverted at user request to the original photographic v2 exports (IMG_4830), before imagegen enhancement and recomposition. Welcome and Secondary enhancements remain in place.

ECA replacement: authentic supplied table-tennis photo, sRGB conversion, saturation reduced 3% and light conventional sharpening. Crop removes the rightmost girl and a small amount at left, as requested. No generative editing.

FS latest approved selection: fresh generation from the original IMG_4830.PNG and supplied crest reference, superseding earlier versions and the temporary original-photo revert. Square composition and original walking posture on right. Responsive v5 WebP exports: 480px / 41290 bytes, 960px / 110880 bytes, 1254px / 153330 bytes.

Secondary first photo: user-requested approximately 10% tighter crop, top-aligned to preserve the maths display, exported as v4 WebP variants. Existing frame dimensions retained.

Secondary photo allocation update: homepage Secondary card now uses science-practical v2, right-aligned (100% 0%). The enhanced science-independent v4 image is the temporary placeholder in the Secondary page’s Expectations and challenge section. No duplicated placement.

Final Secondary maths crop: additional 15% zoom after the requested 10%, totalling 1.265x; v5 exports supersede the unpublished v4 crop.
