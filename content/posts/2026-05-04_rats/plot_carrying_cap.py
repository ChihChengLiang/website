import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

r_b = 0.6;  r_c = 0.02
p_b = 0.01; p_d = 0.4
R0, P0 = 40, 10
R_eq = p_d / p_b   # 40
P_eq = r_b / r_c   # 30
T    = 2 * np.pi / np.sqrt(r_b * p_d)

def lv_standard(t, y):
    R, P = y
    return [r_b * R - r_c * R * P,
            p_b * R * P - p_d * P]

def lv_logistic(K):
    def f(t, y):
        R, P = y
        return [r_b * R * (1 - R / K) - r_c * R * P,
                p_b * R * P - p_d * P]
    return f

T_sim = 8 * T
t = np.linspace(0, T_sim, 4000)

# baseline + three K values
scenarios = [
    ("no cap (baseline)",  None,  "#888888", "--"),
    ("$K = 200$",          200,   "#2471a3", "-"),
    ("$K = 80$",           80,    "#e67e22", "-"),
    ("$K = 50$",           50,    "#c0392b", "-"),
]

results = []
for label, K, color, ls in scenarios:
    fn  = lv_standard if K is None else lv_logistic(K)
    sol = solve_ivp(fn, [0, T_sim], [R0, P0], max_step=0.05, dense_output=True)
    R_t, P_t = sol.sol(t)
    results.append((label, K, color, ls, R_t, P_t))

# ── Style ──────────────────────────────────────────────────────────────────
DIM_C = "#7f8c8d"
plt.rcParams.update({
    "figure.facecolor": "none",
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

fig = plt.figure(figsize=(10, 4.2))
gs  = gridspec.GridSpec(1, 2, figure=fig, wspace=0.38,
                        left=0.08, right=0.97, top=0.87, bottom=0.13)

# ── Left: rats over time ───────────────────────────────────────────────────
ax1 = fig.add_subplot(gs[0])
for label, K, color, ls, R_t, P_t in results:
    lw = 1.4 if K is not None else 1.2
    ax1.plot(t, R_t, color=color, lw=lw, ls=ls, label=label)

ax1.axhline(R_eq, color="#aaaaaa", lw=0.8, ls=":", zorder=0)
ax1.text(T_sim * 0.98, R_eq + 1.5, f"$R^* = {R_eq:.0f}$",
         ha="right", fontsize=7.5, color="#aaaaaa")

ax1.set_xlabel("time")
ax1.set_ylabel("rat population $R$")
ax1.set_title("rats — does $K$ cap the peak?", pad=8)
ax1.legend(framealpha=0, fontsize=8)
ax1.grid(True, axis="y")
ax1.spines[["top", "right"]].set_visible(False)

# ── Right: zoom on first two peaks ────────────────────────────────────────
ax2 = fig.add_subplot(gs[1])
zoom_end = 2.5 * T
mask = t <= zoom_end
for label, K, color, ls, R_t, P_t in results:
    lw = 1.6 if K is not None else 1.2
    ax2.plot(t[mask], R_t[mask], color=color, lw=lw, ls=ls, label=label)

ax2.axhline(R_eq, color="#aaaaaa", lw=0.8, ls=":", zorder=0)
ax2.set_xlabel("time")
ax2.set_ylabel("rat population $R$")
ax2.set_title("zoom: first two cycles", pad=8)
ax2.legend(framealpha=0, fontsize=8)
ax2.grid(True, axis="y")
ax2.spines[["top", "right"]].set_visible(False)

fig.suptitle(
    f"Lotka–Volterra with carrying capacity  ·  $R_0={R0}$, $P_0={P0}$"
    f"  ·  $R^*={R_eq:.0f}$",
    fontsize=9.5, y=0.97, color="#444444",
)

out = "lotka_volterra_cap.png"
fig.savefig(out, dpi=160, bbox_inches="tight", transparent=True)
print(f"Saved → {out}")
