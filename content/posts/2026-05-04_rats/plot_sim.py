import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Parameters from the article
r_b = 0.6   # rat birth rate
r_c = 0.02  # predation rate
p_b = 0.01  # predator growth rate
p_d = 0.4   # predator death rate

R0, P0 = 40, 10
R_eq = p_d / p_b   # = 40
P_eq = r_b / r_c   # = 30
T    = 2 * np.pi / np.sqrt(r_b * p_d)  # ≈ 12.8

def lotka_volterra(t, y):
    R, P = y
    return [r_b * R - r_c * R * P,
            p_b * R * P - p_d * P]

sol = solve_ivp(lotka_volterra, [0, 4 * T], [R0, P0],
                max_step=0.05, dense_output=True)
t      = np.linspace(0, 4 * T, 2000)
R, P   = sol.sol(t)

# ── Colours (legible on white, light-gray, or off-white) ───────────────────
RAT_C  = "#c0392b"   # deep red
PRED_C = "#2471a3"   # steel blue
EQ_C   = "#1e8449"   # forest green
DIM_C  = "#7f8c8d"   # gray for annotations / ticks

plt.rcParams.update({
    "figure.facecolor": "none",   # transparent — inherits page bg
    "axes.facecolor":   "none",
    "axes.edgecolor":   "#cccccc",
    "axes.labelcolor":  "#333333",
    "xtick.color":      DIM_C,
    "ytick.color":      DIM_C,
    "grid.color":       "#e5e5e5",
    "grid.linewidth":   0.7,
    "text.color":       "#222222",
    "font.family":      "sans-serif",
    "font.size":        9,
})

fig = plt.figure(figsize=(7, 4.5))
gs  = gridspec.GridSpec(1, 1, figure=fig,
                        left=0.09, right=0.97, top=0.87, bottom=0.13)

# ── Left: time series ──────────────────────────────────────────────────────
ax1 = fig.add_subplot(gs[0])
ax1.plot(t, R, color=RAT_C,  lw=2.0, label="rats $R$")
ax1.plot(t, P, color=PRED_C, lw=2.0, label="predators $P$")

ax1.axhline(R_eq, color=RAT_C,  lw=0.9, ls="--", alpha=0.4)
ax1.axhline(P_eq, color=PRED_C, lw=0.9, ls="--", alpha=0.4)

ax1.scatter([0], [R0], color=RAT_C,  s=45, zorder=5)
ax1.scatter([0], [P0], color=PRED_C, s=45, zorder=5)

for k in range(1, 5):
    ax1.axvline(k * T, color="#dddddd", lw=0.8, ls=":")
    ax1.text(k * T, -9, f"$T\\!\\times\\!{k}$",
             ha="center", fontsize=7, color=DIM_C)

ax1.annotate(f"$R^* = {R_eq:.0f}$", xy=(t[-1] * 0.97, R_eq + 1.5),
             ha="right", fontsize=7.5, color=RAT_C)
ax1.annotate(f"$P^* = {P_eq:.0f}$", xy=(t[-1] * 0.97, P_eq + 1.5),
             ha="right", fontsize=7.5, color=PRED_C)

ax1.set_xlabel("time")
ax1.set_ylabel("population")
ax1.set_title("population over time", pad=8)
ax1.legend(framealpha=0)
ax1.grid(True, axis="y")
ax1.spines[["top", "right"]].set_visible(False)


fig.suptitle(
    f"Lotka–Volterra  ·  $r_b={r_b}$, $r_c={r_c}$, $p_b={p_b}$, $p_d={p_d}$"
    f"  ·  period $T \\approx {T:.1f}$",
    fontsize=9.5, y=0.97, color="#444444",
)

out = "lotka_volterra_demo.png"
fig.savefig(out, dpi=160, bbox_inches="tight", transparent=True)
print(f"Saved → {out}")
