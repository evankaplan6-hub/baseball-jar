# Baseball jar

Estimating how many baseballs are in FanDuel's "Home of Home Runs Jar" (guess the count, closest without going over wins a 2027 World Series trip; entries run through the last day of the 2026 World Series). Nothing has been submitted.

## Where it stands

| Scale source | Median | 90% range | Implied jar height |
|---|---|---|---|
| **Anchor**: FanDuel's stated height (74 11/16 in) | **5,643** | 4,912 to 6,462 | 74.7 in (matches) |
| **Ball size**: blind measurement of the balls (about 124 px each) | **7,835** | 6,507 to 9,450 | 83.2 in (does not match) |

The two disagree by about 40%, and **that disagreement is not resolved.** The anchor scenario was the working answer (about 5,650) because it reproduces the one hard number FanDuel published. The last independent check, a blind measurement of ball size against synthetic packings, read the balls about 10% smaller in pixels than the anchor predicts. If that reading is right, the count is nearer 7,800. The earlier summary of the 5,650 estimate was written before that check came back.

What would settle it:

- A tape measure across one panel of the real jar, or a photo of a person of known height beside it.
- Counting whole balls along a row of known pixel length on the face-on panel. This does not depend on shading. It was in progress when the earlier work stopped.

## How the estimate is built

`count = packing x jar volume / ball volume`

- The jar is an octagonal prism. Octagon side is about 21.0 in post to post, about 48.8 in flat to flat inside, fill about 61 in at the glass.
- Packing fraction is 0.59, plus or minus 0.02. Ball diameter is 2 7/8 in, as FanDuel's own graphic labels it.
- Sizes come from pixel measurements on the 26-frame studio spin of the jar (4284 x 5712 photos, hosted by the display fabricator). The two scenarios differ only in the pixels-per-inch scale used to convert them.
- A check on the cork lid, the two rails and the glass: at the anchor scale they add up to 74.7 in against the stated 74.69 in.

`jar_estimate.py` reruns the whole thing (400,000 draws, a few seconds).

```bash
python3 jar_estimate.py
```

It needs `numpy`.

## Source images

`images/` holds the 26 studio-spin photos at full 4284 x 5712 resolution, their original EXIF records, and FanDuel's dimension graphic (6 ft 2 11/16 in tall, 2 7/8 in balls). They belong to FanDuel and the fabricator. `images/README.md` says where each one came from.

## Not in this repo

The pixel-measurement scripts, which were scratch files and are gone. The pixel measurements they produced are the numbers hard-coded in `jar_estimate.py`.
