# A Count Without Numbers

**The √2 spiral, its folded dimension, and why it is not Fibonacci**

Maayan Keynan · Independent Researcher · ORCID [0009-0000-5586-4365](https://orcid.org/0009-0000-5586-4365)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22916487.svg)](https://doi.org/10.5281/zenodo.22916487)

An elementary construction of a square-generation spiral in which each generation
is obtained from the previous one by scaling by √2 and turning through 45°. The
construction is deliberately *numberless*: it is generated as a single continuous
directional stroke whose lengths are fixed not by measurement but by one rule, that
each cycle returns to a shared origin. The generator is the Gaussian integer 1 + i,
so the figure is the orbit of the unit square under z ↦ (1 ± i) z. From this single
object the paper reads three things: a folded (transitional) dimension, an
invariance under the shape of the unit, and a clean separation from both the golden
(logarithmic) spiral and the Fibonacci square construction. None of the underlying
geometry is new; the contribution is a unified, elementary way of seeing it.

## This repository

This is the public mirror of the archived record on Zenodo: version DOI [10.5281/zenodo.22916487](https://doi.org/10.5281/zenodo.22916487).

- **`Keynan_2026_A_Count_Without_Numbers.pdf`** — the paper.
- **`supplementary/`** — companion materials:
  - `Video_S1_single_stroke_animation.mp4` — the construction drawn as one continuous stroke.
  - `draw_root_spiral.py` — self-contained code (numpy + matplotlib) that draws the spiral from the generator 1 + i.
  - `drawn_root_spiral.png` — the figure produced by that code.
  - `construction_primer.png` — a step-by-step build of the stroke.
  - `figs_pub/` — the paper's five figures at full resolution.
  - `README.md` — describes each file.

## Cite

> Keynan, M. (2026). *A Count Without Numbers: the √2 spiral, its folded dimension,
> and why it is not Fibonacci.* Zenodo. https://doi.org/10.5281/zenodo.22916485 (concept DOI — always resolves to the latest version)

## License

Paper, figures, video and data: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), matching the Zenodo record. Code (`supplementary/draw_root_spiral.py`): [MIT License](LICENSE).
