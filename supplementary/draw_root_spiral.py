#!/usr/bin/env python3
"""
draw_root_spiral.py  —  companion code for
"A Count Without Numbers: the √2 spiral, its folded dimension, and why it is not Fibonacci"
(Maayan Keynan, Independent Researcher, ORCID 0009-0000-5586-4365).

Draws the √2 spiral directly from the paper's generator, with no external
inputs. The figure is the orbit of the unit square under z ↦ (1 + i) z:
each generation is the previous one scaled by √2 and turned through 45°.
Run it and it writes drawn_root_spiral.png next to itself.

Requires only numpy and matplotlib (pip install numpy matplotlib).
"""

import numpy as np
import matplotlib.pyplot as plt

# ---- the generator ---------------------------------------------------------
# Multiplication by the Gaussian integer 1 + i scales by |1+i| = √2 and
# rotates by arg(1+i) = 45°. So generation n is (1+i)**n times generation 0.
g = 1 + 1j
N = 8                       # number of generations to draw (0 .. N)

# Generation 0 is the unit square with one vertex at the shared origin.
# Vertices as complex numbers, listed around the square and closed.
unit_square = np.array([0, 1, 1 + 1j, 1j, 0], dtype=complex)

# ---- draw ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 7))

for n in range(N + 1):
    square = unit_square * (g ** n)          # the whole orbit, one line
    ax.plot(square.real, square.imag, color="#c0392b", lw=1.6, zorder=2)
    # shade the folded (odd-power / 45°-offset) generations
    if n % 2 == 1:
        ax.fill(square.real, square.imag, color="#3498db", alpha=0.18, zorder=1)
    # label each generation near its outer vertex (1+i)*g**n
    tip = (1 + 1j) * (g ** n)
    ax.annotate(str(n), (tip.real, tip.imag), color="#1f3a5f",
                fontsize=11, ha="center", va="center", zorder=3)

# the equiangular spiral the outer corners lie on: r(theta) = r0 * 2**(theta/(pi/2)).
# The outer corner of generation n is (1+i)*g**n; interpolate n continuously.
t = np.linspace(0, N, 600)
curve = (1 + 1j) * (g ** t)
ax.plot(curve.real, curve.imag, color="#7f8c8d", lw=1.0, ls="--", zorder=2)

ax.set_aspect("equal")
ax.axis("off")
ax.set_title("The √2 spiral: the orbit of the unit square under z ↦ (1 + i) z\n"
             "(dashed: the logarithmic spiral through the outer corners; "
             "shaded: the folded, odd-power generations)",
             fontsize=9)

out = "drawn_root_spiral.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("wrote", out)
