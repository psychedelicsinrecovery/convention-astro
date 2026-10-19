# 🖼️ assets - the Convention raster shelf

This folder is the one home for artwork and rasters made for the Convention suite
(marquee tiles, session thumbnails, ceremony art). Anne's pixel-art rasters live here -
the sunset-over-the-mountains series with the eye-in-diamond, drawn in her style.

**Heads-up, dear reader:** GitHub Pages for this site only publishes what the Astro
build puts in `public/`, so a file parked here is a *shelf* copy - it is kept in the
repository for the fellowship to see and reuse, but it is not served to the live site
from here. When a raster goes live (the recordings marquee, a page banner), its
serving copy lives in the WordPress media library or in `public/`, and the page
references it there. Keep both in step when you swap art.

New here? The friendly walkthrough for adding pictures to a shelf like this one lives
in the gallery repo: [walkthrough-astrolog.html](https://psychedelicsinrecovery.github.io/gallery/walkthrough-astrolog.html).

## How to add a raster (the 60-second version)

1. Go to this repo on GitHub, open the `assets` folder, click **Add file -> Upload files**. (Or press `.` on the repo page to open github.dev and drag the file in.)
2. Name the file first, following the convention below (you can rename in the upload dialog).
3. Commit to `main`. The shelf is browsable by anyone in the fellowship, no code needed.

## Naming convention (please keep it)

`YYYY-MM-DD-short-name.png` - the date the artwork was made, not the day you upload it.

Examples:

- `2026-10-19-opening-ceremony.png`
- `2026-10-19-steps-workshop.png`

## Using a raster on the site

Reference the serving copy by its public URL (WordPress media library or `public/`),
always with an `alt` that describes what a person would see. One image, one home per
purpose: the shelf keeps the original, the site references the optimized copy.

## Size care

Full-resolution PNG rasters can run large. The marquee uses the optimized 1280x720
JPEG copies so phones load them happily - keep optimized copies alongside originals
when a raster is headed for a live page.

## Why one folder

Artwork lives here rather than scattered through the source so that anyone in the
fellowship can contribute without touching code: upload, name it well, done. The
build never reads this folder - it simply carries it - so an image can never break
the site.
