"""
康托尔魔鬼楼梯 (Cantor's Devil's Staircase)

康托尔函数 F(x) 是 [0,1] 上的一个连续、单调递增的函数，
值域也是 [0,1]。但它几乎处处导数为 0 —— 它的增长完全集中在
康托尔集上，而康托尔集的勒贝格测度为 0。

这使得它在视觉上既像连续的又像离散的阶梯，
难以直观区分它是连续分布还是离散分布。
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

rcParams["font.sans-serif"] = ["WenQuanYi Micro Hei", "Noto Sans CJK SC", "SimHei",
                                 "Arial Unicode MS", "DejaVu Sans"]
rcParams["axes.unicode_minus"] = False


def cantor_function(x, depth=10):
    """
    通过迭代构造计算康托尔函数值。

    在每一步中，把 [0,1] 分成三等份，去掉中间的三分之一，
    左段映射到 [0, 0.5]，右段映射到 [0.5, 1]，反复迭代。
    """
    x = np.asarray(x, dtype=float)
    result = np.zeros_like(x)

    for d in range(depth):
        step = 3.0 ** (d + 1)
        mask = (x * step % 1 >= 1.0 / 3.0) & (x * step % 1 < 2.0 / 3.0)
        # 在被去掉的"中间三分之一"区间上，函数值保持不变
        # 这些点的贡献已经在之前更粗的迭代中确定了
        result[~mask] += (1.0 / 2.0) ** (d + 1) * (
            np.floor(x[~mask] * step) % 3
        )

    # 对仍在"中间"的点，赋予上一步的端点值
    for d in range(depth):
        step = 3.0 ** (d + 1)
        for i in range(len(x)):
            frac = x[i] * step % 1
            if 1.0 / 3.0 <= frac < 2.0 / 3.0:
                base = np.floor(x[i] * step)
                left_val = base + 1.0 / 3.0
                left_val /= step
                result[i] = cantor_function(np.array([left_val]), d)[0]
                break

    return result


def cantor_function_iterative(x, max_depth=12):
    """
    更高效的实现：利用三进制表示。

    对于 x in [0,1]，写出三进制展开 0.a1 a2 a3 ...
    - 若第一个数字为 1，则 F(x) = 1/2
    - 若前两个数字为 0,1 则 F(x) = 1/4
    - 一般地，找到第一个 1 的位置 k，F(x) = (二进制 0.b1...b_{k-1}1)
      其中 bi 是去掉那个 1 之前的 0/2 对应的二进制位
    - 若三进制展开中没有 1（即 x 属于康托尔集），
      则将所有 2 替换为 1 得到二进制数即为 F(x)
    """
    x = np.asarray(x, dtype=float)
    result = np.zeros_like(x)

    for i in range(len(x)):
        xi = x[i]
        if xi <= 0:
            result[i] = 0.0
        elif xi >= 1:
            result[i] = 1.0
        else:
            binary_frac = 0.0
            power = 0.5
            found_one = False
            for k in range(max_depth):
                xi *= 3.0
                digit = int(xi)
                xi -= digit
                if digit == 1:
                    binary_frac += power  # 遇到 1 就终止，加上这一位
                    found_one = True
                    break
                elif digit == 2:
                    binary_frac += power
                power *= 0.5
            if not found_one:
                # x 属于康托尔集，binary_frac 已经是精确值
                pass
            result[i] = binary_frac

    return result


def plot_devils_staircase():
    """绘制康托尔魔鬼楼梯，展示不同精度的逼近。"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    fig.suptitle("Cantor's Devil's Staircase", fontsize=18, fontweight="bold")

    depths = [3, 6, 9, 12]
    n_points = 100000

    x = np.linspace(0, 1, n_points)

    for idx, (ax, depth) in enumerate(zip(axes.flat, depths)):
        y = cantor_function_iterative(x, max_depth=depth)

        ax.plot(x, y, color="#2c3e50", linewidth=0.4)
        ax.fill_between(x, 0, y, alpha=0.08, color="#3498db")

        # 标注水平平台（阶梯）
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.02, 1.02)

        # 画 y=x 对角线作参考
        ax.plot([0, 1], [0, 1], "--", color="#e74c3c", alpha=0.4, linewidth=0.8,
                label="y = x")

        ax.set_title(f"Depth = {depth}", fontsize=13)
        ax.set_xlabel("x", fontsize=11)
        ax.set_ylabel("F(x)", fontsize=11)
        ax.legend(fontsize=9, loc="upper left")
        ax.grid(True, alpha=0.2)

        # 标注关键性质
        if depth >= 9:
            info_text = (
                "Continuous\n"
                "Monotone increasing\n"
                "F'(x) = 0 a.e.\n"
                "Lebesgue growth = 0\n"
                f"Points: {n_points}"
            )
        else:
            info_text = f"Points: {n_points}"
        ax.text(0.98, 0.02, info_text, transform=ax.transAxes,
                fontsize=8, verticalalignment="bottom", horizontalalignment="right",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="wheat", alpha=0.5))

    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, "devils_staircase.png"), dpi=200, bbox_inches="tight")
    plt.show()


def plot_single_high_quality():
    """绘制一张高质量的魔鬼楼梯图。"""
    fig, ax = plt.subplots(figsize=(10, 7))

    n_points = 200000
    x = np.linspace(0, 1, n_points)
    y = cantor_function_iterative(x, max_depth=14)

    # 主曲线
    ax.plot(x, y, color="#2c3e50", linewidth=0.3, label="Cantor Function F(x)")

    # 标注被去掉的区间 (前几级)
    colors = ["#e74c3c", "#e67e22", "#f1c40f", "#2ecc71"]
    for level in range(4):
        seg_len = 1.0 / (3 ** (level + 1))
        n_segs = 3 ** level
        for j in range(n_segs):
            left = (3 * j + 1) * seg_len
            right = (3 * j + 2) * seg_len
            mid_y = cantor_function_iterative(
                np.array([(left + right) / 2]), max_depth=14
            )[0]
            ax.plot(
                [left, right], [mid_y, mid_y],
                color=colors[level], linewidth=2.5, alpha=0.7,
                label=f"Level {level+1}" if j == 0 else None,
            )

    # 参考线
    ax.plot([0, 1], [0, 1], "--", color="#95a5a6", linewidth=0.8, label="y = x")

    # 关键点标注
    for val in [1/3, 2/3]:
        fy = cantor_function_iterative(np.array([val]), max_depth=14)[0]
        ax.plot(val, fy, "o", color="#e74c3c", markersize=5, zorder=5)
        ax.annotate(
            f"({val:.2f}, {fy:.2f})",
            xy=(val, fy),
            xytext=(val + 0.05, fy + 0.06),
            fontsize=9,
            arrowprops=dict(arrowstyle="->", color="#e74c3c"),
        )

    ax.set_title("Cantor's Devil's Staircase", fontsize=16, fontweight="bold")
    ax.set_xlabel("x", fontsize=13)
    ax.set_ylabel("F(x)", fontsize=13)
    ax.legend(fontsize=10, loc="upper left")
    ax.grid(True, alpha=0.15)
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.02, 1.05)

    # 性质说明
    props = (
        "Properties:\n"
        "  * Continuous everywhere\n"
        "  * Monotone non-decreasing\n"
        "  * F(0)=0, F(1)=1\n"
        "  * F'(x) = 0 almost everywhere\n"
        "  * Not absolutely continuous\n"
        "  * Singular continuous CDF"
    )
    ax.text(
        0.98, 0.45, props,
        transform=ax.transAxes, fontsize=10,
        verticalalignment="top", horizontalalignment="right",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.8),
    )

    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, "devils_staircase_hq.png"), dpi=200, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    print("绘制多精度逼近图...")
    plot_devils_staircase()
    print("绘制高质量单图...")
    plot_single_high_quality()
    print("完成！图像已保存为 devils_staircase.png 和 devils_staircase_hq.png")
