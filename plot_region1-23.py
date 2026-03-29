import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 6))

# Draw the unit square [0,1] x [0,1]
square = plt.Polygon([[0, 0], [1, 0], [1, 1], [0, 1]],
                      fill=False, edgecolor='black', linewidth=2)
ax.add_patch(square)

# Fill the region: inside unit square AND x + y < 1.4
x = np.linspace(0, 1, 500)
y_upper = np.minimum(1, 1.4 - x)  # clip by y=1 (top of square)
y_lower = np.zeros_like(x)
ax.fill_between(x, y_lower, y_upper, alpha=0.3, color='steelblue',
                label=r'$\{x+y<1.4\}\cap[0,1]^2$')

# Draw the line x + y = 1.4 (clipped to the unit square)
# Intersections with square boundary: (0, 1.4) -> clipped to (0, 1); (0.4, 1); (1, 0.4)
line_x = [0.4, 1]
line_y = [1, 0.4]
ax.plot(line_x, line_y, 'r--', linewidth=2, label=r'$x+y=1.4$')

ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.05, 1.05)
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Region: $x+y<1.4$ within $[0,1]^2$')
ax.legend(loc='upper right')
ax.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.savefig('./region_plot.png', dpi=150)
plt.show()
