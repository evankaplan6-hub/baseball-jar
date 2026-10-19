# Source images

These belong to FanDuel and the display fabricator. They are here so the measurements in this repo can be checked against the same pixels.

## `spin/Image_1.jpg` to `Image_26.jpg`

The 26 frames of the jar's 360° studio spin, 4284 x 5712 px each, downloaded 2026-10-19 from the fabricator's Sirv CDN:

```
https://experiencerevere.sirv.com/FanDuel%20%20Jar%20-%20Blue%20Background%20%232/Image%201.jpg
```

(`Image%201.jpg` through `Image%2026.jpg`). They are saved byte for byte as served, and each file size matches the `content-length` in `spin-metadata/http_headers/`.

Sirv re-encodes images and strips camera EXIF when it serves them, so these are full resolution but not the photographer's untouched files.

## `spin-metadata/`

- `exif/Image_N.json`: Sirv's `?info` record for each frame. It still carries the original file's EXIF (iPhone 17 Pro, lens, focal length, capture time).
- `spin_info.json`: the spin's frame list and viewer settings.
- `http_headers/hdr_N.txt`: the server's response headers for each download.

## `dimension_graphic.png`

A 1080 x 1920 frame at 14.0 s of [FanDuel's video on X](https://x.com/FanDuel/status/2110884433226031346). The inset graphic shows:

- "6 FEET 2 11/16″ TALL", with the arrow running from the top of the cork lid to the bottom of the acrylic body (the plinth and the display ball on top are not included).
- "REGULATION SIZE BASEBALL 2 7/8″ (2.875″)".
