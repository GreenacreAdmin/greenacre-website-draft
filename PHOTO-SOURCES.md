# Website photo selections

Updated 11 October 2026. There are 27 photography-checklist slots; a photograph may be reused where requested. Logos and staff-roster portraits are outside this list.

This register reflects the latest user-selected photos for Campus, Secondary, Primary, Early Years, About Greenacre, Curriculum and the swimming pool. Primary photo 1 and Early Years photo 2 remain unchanged. All newly supplied images use conventional colour correction and responsive WebP exports; no generative image editing was used for this replacement set.

## Homepage

| Frame | Source | Served asset |
|---|---|---|
| Hero | Existing approved seedlings image; retained | `assets/images/optimized/home-hero-seedlings-v3.*` |
| intro-photo | `IMG_4518.PNG` | `assets/images/school-2026/individual-support-*.webp`; 50% 35% |
| phase-card.early::before | `IMG_4830.PNG` | `assets/images/school-2026/early-years-nature-*.webp` |
| phase-card.primary::before | [https://www.greenacre.ac.th/](https://www.greenacre.ac.th/) | `assets/images/school-2026/reading-together-*.webp` |
| phase-card.secondary::before | `IMG_5037.PNG` | `assets/images/school-2026/science-practical-*.webp`; 100% 0% |
| identity-photo | Swapped with Environmentality "Our values in action" on 11 October 2026 | `assets/images/school-2026/environment-garden-v1-*-colour-v1.webp`; 50% 38% |

## Internal pages

| Page / photo slot | Source | Served asset / crop |
|---|---|---|
| `learning/curriculum/` / 1 | Reused from Work With Us | `assets/images/recruitment/teacher-with-pupils-*.webp`; bottom-aligned 3:2 crop |
| `learning/curriculum/` / 2 | `IMG_4117.HEIC` | `assets/images/school-2026/primary-art-*.webp`; 50% 100% |
| `learning/early-years/` / 1 | `IMG_6830.HEIC` | `assets/images/school-2026/early-years-drawing-*.webp`; 50% 47% |
| `learning/early-years/` / 2 | `IMG_5471.PNG` (supplied 11 October 2026) | `assets/images/school-2026/early-years-dough-*.webp`; bottom-aligned 3:2 crop, 50% 100% |
| `learning/primary/` / 1 | `IMG_5023.PNG` | `assets/images/school-2026/primary-teaching-*.webp`; 50% 15% |
| `learning/primary/` / 2 | `IMG_5472.PNG` | `assets/images/school-2026/primary-garden-learning-*.webp`; 50% 0% |
| `learning/secondary/` / 1 | `IMG_5461.PNG` (supplied 11 October 2026) | `assets/images/school-2026/secondary-laptops-*.webp`; 3:2 crop, 50% 50% |
| `learning/secondary/` / 2 | `IMG_5603.HEIC` | `assets/images/school-2026/secondary-practical-*.webp`; 50% 50% |
| `learning/clubs-ecas/` / 1 | User-supplied `unnamed (2).jpg` | `assets/images/school-2026/table-tennis-*.webp`; 25% 50% |
| `our-school/about-greenacre/` / 1 | `IMG_4998.PNG` (reused from Admissions / “Start with a visit”) | `assets/images/school-2026/classroom-welcome-*.webp`; 50% 55% |
| `our-school/campus-facilities/` / 1 | `IMG_5700.PNG` | `assets/images/school-2026/campus-walkway-*.webp`; 50% 50% |
| `our-school/campus-facilities/` / 2 | `IMG_5544.PNG` | `assets/images/school-2026/campus-courts-*.webp`; 50% 50%; displayed in the same 3:2 style as the other content photos |
| `our-school/campus-facilities/` / 3 | George-supplied `IMG_5485.HEIC` (5286x3964, 16 Oct 2026; replaces the 11 Oct pool photo) | `assets/images/school-2026/swimming-pool-long-*-v3.webp` desktop (8:3 crop, full width, rows 1220-3202) and `swimming-pool-mobile-*-v3.webp` at 640px and below (16:9 crop, 600,1200-4680,3495, closer on the swimmers and teacher). Display P3 converted to sRGB, levels stretched (0.3%/99.7% luminance), saturation x1.12, no sharpening; WebP quality 70. Desktop set 25/97/213 KB, mobile set 37/143/278 KB |
| `our-school/environmentality/` / 1 | [Current school site](https://www.greenacre.ac.th/home) | `assets/images/current-site/home-02.webp` |
| `our-school/environmentality/` / 2 ("Our values in action") | User-selected imagegen edit of `IMG_4188.HEIC`, swapped from the homepage on 11 October 2026 | `assets/images/school-2026/watering-together-*.webp`; 50% 50% |
| `our-school/wellbeing/` / 1 | [Current school site](https://www.greenacre.ac.th/extra-curricular/wellbeing) | `assets/images/current-site/extra-curricular-wellbeing-02.webp` |
| `our-school/wellbeing/` / 2 | `IMG_5038.PNG` | `assets/images/school-2026/outdoor-chess-*.webp`; 50% 72% |
| `admissions/admissions-visits/` / 1 | George-supplied `IMG_5542.png` (1448x1086, 25 Oct 2026; staff member showing visiting families around the grounds, permissions obtained by George; replaces the 24 Oct picket-fence photo) | `assets/images/school-2026/admissions-visit-tour-*-v2.webp`; 3:2 crop rows 80-1045, 50% 50%. Site recipe: luminance levels stretch, saturation x1.12, WebP quality 70: set 32/97/162 KB. The image sits in the first screen, so it loads straight away (`fetchpriority="high"`, not lazy). Earlier fence, tour v1 and plant photo files kept unused |
| `parent-information/services/` / 1 | [Current school site](https://www.greenacre.ac.th/academics/environmentality) | `assets/images/current-site/academics-environmentality-02.webp` |
| `our-school/head-of-school-welcome/` / 1 | `1742964487955 (1).jpg` | `assets/images/school-2026/head-dara-nagle-*.webp`; 50% 0% |
| `work-with-us/` / 1 | `work with us.png` (sharper version supplied 11 October 2026) | `assets/images/recruitment/teacher-easel-*.webp`; 3:2 crop, 50% 50%. The earlier teacher-and-pupils photo remains on Curriculum |

## Crop and delivery notes

- Original ZIP and separate portrait remain outside the deployed repository. New web assets are full-frame WebP derivatives at 480, 960 and up to 1440 pixels wide, with no upscaling. HTML `srcset` and homepage CSS `image-set` serve responsive versions.
- The existing frame sizes, border treatments, spacing and responsive layouts are retained. Individual images use crop positions that keep the main faces and interaction visible.
- The Head of School portrait keeps the previous displayed ratio of 902:1327; it is cropped within that frame.
- Sand play is used only on the Early Years page. The 3:2 crop prioritises both faces and the activity; it cannot retain the whole bowl from the tight original.
- `IMG_5026.JPG` remains a reserve because its portrait composition fits the ordinary landscape frames poorly. The two `IMG_4218` versions are already represented by Work with Us and are not added elsewhere.
- All replacement badges have been removed from the selected photo frames, including intentionally retained images.
- Parent Services retains a produce photograph as a food-related illustration. It is not labelled as dining. A dedicated dining image would still improve specificity.

## Staff roster portraits

- `our-school/our-team/` / Mr Dara: new HEIC portrait supplied 11 October 2026; sRGB, cropped closer to a head-and-shoulders circle to match the roster, 570 × 570 circular transparent PNG master in `assets/images/team/dara.png`, served as `assets/images/optimized/team-dara-v2.webp`. The Head of School welcome page photo is unchanged.
- `our-school/our-team/` / Mr Mark: original `Mark.HEIC` (re-supplied 11 October 2026); sRGB, full-width square crop framed to match Mr Dara, with a light warm (yellow) and saturation lift, 570 × 570 circular transparent PNG master in `assets/images/team/mark.png`, served as `assets/images/optimized/team-mark-colour-v5.webp`.
- `our-school/our-team/` / Ms Tippawan (Tip): re-cropped about 15% tighter on 27 October 2026 from George's re-supplied `Tip.png` (674 × 674 with a baked-in green ring): 485 px square at 75,58, inside the ring, so she sits lower and larger, matching Mr Dara and Mr Mark. Master `assets/images/team/tip-v2.png` is the standard 570 × 570 circular transparent PNG. The served `assets/images/optimized/team-tip-v2.webp` is made straight from the 485 px crop at 384 × 384 with transparency, WebP quality 90, 26 KB (in line with the other roster portraits). The old files are kept.
- `our-school/our-team/` / Ms Jassy, Mr Josh, Ms Minda: no photo yet; they show the green person-icon placeholder (`.team-avatar-v2--placeholder`).

## Earlier photo-selection history

### Current-site review — 5 October 2026

Reviewed the live homepage, Early Years, Primary, Curriculum, Environmentality, Wellbeing, Swimming Pool, Services, Community and Head of School Welcome pages on 5 October 2026. Strong reading, collaboration, classroom participation, outdoor learning, meditation, produce and pool images were retained or reassigned.

The current homepage reading image was downloaded through the browser asset export and optimised as `reading-together-*.webp`. Other reused photographs were already stored in `assets/images/current-site/`. The supplied new portrait supersedes the live site’s lectern photograph.

## Verification

- Visual review at browser viewport widths 1440, 768 and 390 pixels.
- No horizontal overflow or missing photo assets across the 13 selected pages.
- Existing ordinary-content and homepage frame dimensions preserved at all three sizes; portrait ratio explicitly preserved.
- Site checker verifies all 49 pages, relative links, fragments, search metadata and original document checksums.
- No push or deployment was performed as part of the 5 October local update.

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

FS v6 colour refinement: conventional selective green hue shifted gently towards yellow with slight saturation increase to match the Primary card; skin hues excluded. No additional generative editing.

Secondary maths v6: same crop scale, shifted downward to regain more of the pupils and desks and remove more from the top, at user request.

## Site-wide conventional colour pass, 7 October 2026

Reviewed rendered photographs at desktop and mobile sizes, including CSS background images and homepage card pseudo-elements. The `-colour-v1` assets use restrained, individually selected saturation, RGB balance and feathered green adjustments. This pass uses no ImageGen, content reconstruction, denoising, sharpening, cropping or resizing. Photographs already consistent with the site were retained. Different fabrics and lighting retain natural variation.

Adjusted exports embed sRGB. Content WebP files use quality 92; the six adjusted staff portraits use lossless WebP, with unchanged alpha and opaque outer-border pixels checked against the originals. Existing photo dimensions, responsive sizing, object positions and layout are unchanged. Original assets remain available. The social preview uses the corrected homepage hero; its metadata generator was updated accordingly.

Adjustment settings and output paths: `scripts/photo-colour-pass-2026-10-07.json`. Original backups, lossless corrected masters, before/after sheets and browser QA are retained in the workspace at `output/colour-pass-2026-10-07/` outside this deployment repository.

Conventions consulted: [Adobe: sRGB for online viewing](https://helpx.adobe.com/ca/photoshop/using/color-managing-documents-online-viewing.html) and [Adobe: white balance and neutral tones](https://www.adobe.com/au/creativecloud/photography/discover/white-balance.html).

## User-selected photo updates — 11 October 2026

- Replaced the selected internal-page photos with the sources listed above. Primary photo 1, Early Years photo 2 and all unrelated photos remain as previously selected.
- Campus photo 2 now uses the standard 3:2 frame. The swimming-pool image uses art-directed 16:6 desktop and 16:9 mobile source crops inside the existing responsive section, with left alignment at narrower widths to retain the instructor.
- About Greenacre photo 1 reuses the classroom image from Admissions / “Start with a visit”.
- Curriculum photo 1 now reuses the Work With Us teacher-and-pupils image, with the same bottom-aligned crop.
- Mr Mark's team portrait uses the supplied `Mark.HEIC`, prepared in the roster's circular portrait style.
- Visit Greenacre's desktop photo now matches the neighbouring campus photo's rendered width; both keep the shared 3:2 crop.
- Embedded Display P3 sources were converted to sRGB; untagged files were treated as sRGB. Colour was adjusted gently per image, with light output sharpening. No generative editing or upscaling was used. Exact crop boxes, colour adjustments, output dimensions and file sizes are recorded in `assets/images/school-2026/sources.json`.
- Replacements are responsive WebP assets at 480px, 960px and the source-limited maximum width, using quality 80; the swimming-pool variants use quality 78.

## Lunch menu food pictures — 24 October 2026

The lunch menu page (`documents/lunch-menu/`) uses no photos. Its small food icons are Phosphor Icons (duotone weight), MIT licence (`assets/vendor/phosphor-icons/LICENSE`), from the `@phosphor-icons/core` package, inlined as SVG symbols in the page.
