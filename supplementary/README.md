# Supplementary materials — *A Count Without Numbers: the √2 spiral…*

Companion files for the paper. The paper's five figures are embedded in the
main PDF; these files add the moving form of the construction, a runnable
script that reproduces the geometry, and a step-by-step primer.

## Contents

- **`Video_S1_single_stroke_animation.mp4`** — the construction drawn as one
  continuous, no-lift stroke, in order, 32 edges (~30 s). This is the moving
  form of Figure 1: the same figure a hand draws without measuring, without
  lifting the pen, and without axes.
- **`draw_root_spiral.py`** — self-contained code that draws the √2 spiral from
  the generator 1 + i, with no external inputs. Run it (`python draw_root_spiral.py`,
  requires only `numpy` and `matplotlib`) and it writes `drawn_root_spiral.png`.
- **`drawn_root_spiral.png`** — the resulting figure produced by the code: the
  orbit of the unit square under z ↦ (1 + i) z, generations 0–8, with the folded
  (odd-power) generations shaded and the logarithmic spiral through the outer
  corners.
- **`construction_primer.png`** — a step-by-step build of the stroke: the two
  colours (launching body and returning side), the first closed unit square, its
  diagonal √2, and the square raised on that diagonal. A visual companion to §1–§2.
- **`figs_pub/`** — the paper's five figures as high-resolution exports, prepared
  from the author's presentation deck. See the table below.

## Figures (in `figs_pub/`)

| File | Paper | Shows |
|---|---|---|
| `fig1_stroke_marked.png` | Figure 1 | The single stroke, 8 generations; blue bodies (launching diagonals), red returning sides. |
| `fig2_spiral.png` | Figure 2 | The spiral in the R = 16 reference circle; the even (folded) generations shaded. |
| `fig3_series.png` | Figure 3 | The count read off the units: the two interleaved series (a, b) and the eight-direction rose (c). |
| `fig4_crystal_fluid.png` | Figure 4 | Four renderings (square / 1:√2 rectangle × crystal / fluid), 11 generations. |
| `fig5_root_vs_fibonacci.png` | Figure 5 | Apples to apples: √2 vs Fibonacci built by the same 45° rule — crystal (top row), fluid (bottom row). |

## Notes

- The paper credits all classical antecedents openly (see *Relation to known
  constructions* and *References*); the contribution is the unified, elementary
  reading, not the underlying geometry.
- `draw_root_spiral.py` reproduces the geometry from first principles; the paper's
  `figs_pub/` figures were composed from the author's presentation deck.
