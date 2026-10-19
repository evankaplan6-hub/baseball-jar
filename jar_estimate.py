"""Monte Carlo estimate of the number of baseballs in FanDuel's "Home of Home Runs Jar".

Count = packing fraction x jar volume / volume of one ball.

The jar is an octagonal prism. Its size is measured in pixels on the original
4284 x 5712 spin photos, then converted to inches with a px-per-inch scale.
That scale is the weak link, so it is the thing the two scenarios disagree on:

  anchor     scale from FanDuel's stated height (6 ft 2 11/16 in = 74.6875 in,
             cork-lid top to bottom of the acrylic body)
  ball_size  scale from measuring the balls themselves (2 7/8 in each)

Run:  python3 jar_estimate.py
"""
import numpy as np

M = 400_000
rng = np.random.default_rng(5)

BALL_IN = 2.875            # FanDuel's graphic labels the balls 2 7/8 in
STATED_HEIGHT_IN = 74.6875


def simulate(corner_px_per_in):
    """corner_px_per_in: samples of the image scale at the jar's nearest corner."""
    # The panel faces sit a little farther from the camera than the near corner,
    # so they get a slightly smaller scale (measured: 1.6% smaller).
    shrink = rng.normal(0.984, 0.008, M)
    panel = corner_px_per_in * shrink
    front = corner_px_per_in * (1 - (1 - shrink) * 0.5)  # face-on panel, half-way in depth

    # Pixel measurements -> inches
    glass7 = rng.normal(705, 15, M) / 0.924 / panel   # wide panels, yawed 22.5 deg (cos = 0.924)
    glass8 = rng.normal(815, 15, M) / front           # face-on panel
    post = rng.normal(110, 8, M) / corner_px_per_in   # aluminium post face
    side = 0.5 * (glass7 + glass8) + 2 * post         # octagon side, post to post (in)

    inset = rng.normal(0.9, 0.4, M)                   # post intrusion into the interior (in)
    area = 4.8284 * side**2 - 8 * side * inset        # octagon area 2(1+sqrt2)s^2 less the post strips
    fill = rng.normal(2878, 60, M) / panel + rng.uniform(0, 1.5, M)  # fill height at the glass (in)

    volume = area * fill * (1 + rng.normal(0, 0.012, M)) * rng.uniform(0.985, 1.0, M)
    ball_vol = np.pi / 6 * rng.normal(BALL_IN, 0.025, M) ** 3
    packing = rng.normal(0.59, 0.02, M)
    count = packing * volume / ball_vol

    return {
        "count": count,
        "panel_px_per_in": panel,
        "side": side,
        "fill": fill,
        "flat_to_flat": np.sqrt(area / 0.8284),
    }


SCENARIOS = {
    # 74.6875 in spans about 3,630 px at the near corner -> 48.6 px/in
    "anchor": rng.normal(48.6, 0.6, M),
    # blind ball-size measurement: 123.5 +/- 3.5 px per ball at the panel -> 42.96 px/in
    # (converted back to the near-corner scale)
    "ball_size": rng.normal(123.5 / BALL_IN / 0.984, 3.5 / BALL_IN / 0.984, M),
}

THRESHOLDS = (5000, 5391, 5575, 5650, 6001, 6500, 7000, 7500)


def main():
    for name, scale in SCENARIOS.items():
        r = simulate(scale)
        n = r["count"]
        pct = np.percentile(n, [5, 25, 50, 75, 95])
        print(f"== scenario: {name}")
        print(f"   panel scale {r['panel_px_per_in'].mean():.1f} px/in -> ball {BALL_IN * r['panel_px_per_in'].mean():.0f} px")
        print(f"   octagon side {r['side'].mean():.1f} in, flat-to-flat {r['flat_to_flat'].mean():.1f} in, fill {r['fill'].mean():.1f} in")
        print(f"   count median {pct[2]:,.0f}   90% range {pct[0]:,.0f} to {pct[4]:,.0f}   (mean {n.mean():,.0f}, sd {n.std():,.0f})")
        print("   P(truth is above guess):", "  ".join(f"{t:,}: {(n > t).mean():.2f}" for t in THRESHOLDS))
        stack = 3030 / r["panel_px_per_in"].mean() + 258 / r["panel_px_per_in"].mean() + 291 / scale.mean()
        print(f"   height check: glass + rails + cork = {stack:.1f} in  (stated {STATED_HEIGHT_IN} in)")
        print()


if __name__ == "__main__":
    main()
