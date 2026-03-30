import random
import math


def make_triangle(a, b, c):
    """构造三角形：顶点A在原点，B在(a,0)，C由余弦定理确定。返回顶点列表。"""
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    sin_C = math.sqrt(max(0, 1 - cos_C**2))

    Ax, Ay = 0.0, 0.0
    Bx, By = a, 0.0
    Cx, Cy = b * cos_C, b * sin_C

    # 将质心移到原点，方便后续旋转和平移
    cx = (Ax + Bx + Cx) / 3
    cy = (Ay + By + Cy) / 3
    return [(Ax - cx, Ay - cy), (Bx - cx, By - cy), (Cx - cx, Cy - cy)]


def rotate_translate(vertices, theta, y_offset):
    """将顶点绕原点旋转theta弧度，再在y方向平移y_offset。"""
    cos_t, sin_t = math.cos(theta), math.sin(theta)
    result = []
    for x, y in vertices:
        rx = x * cos_t - y * sin_t
        ry = x * sin_t + y * cos_t + y_offset
        result.append((rx, ry))
    return result


def crosses_any_line(vertices, d):
    """检查三角形是否与任何一条水平线 y = k*d 相交。"""
    ys = [v[1] for v in vertices]
    y_min, y_max = min(ys), max(ys)

    k_low = math.floor(y_min / d)
    k_high = math.ceil(y_max / d)

    for k in range(k_low, k_high + 1):
        line_y = k * d
        for i in range(3):
            y1 = vertices[i][1]
            y2 = vertices[(i + 1) % 3][1]
            if (y1 - line_y) * (y2 - line_y) < 0:
                return True
    return False


def simulate(a, b, c, d, n_trials=1_000_000, seed=None):
    """
    蒙特卡洛模拟：三角形(a,b,c)落在间距为d的平行线上，返回相交概率的估计值。
    """
    if seed is not None:
        random.seed(seed)

    assert max(a, b, c) < d, "最大边长必须小于平行线间距d"

    vertices = make_triangle(a, b, c)
    count = 0

    for _ in range(n_trials):
        theta = random.random() * math.pi        # 随机方向角 [0, π)
        y_offset = random.random() * d            # 质心到最近下方线的距离 [0, d)

        rotated = rotate_translate(vertices, theta, y_offset)
        if crosses_any_line(rotated, d):
            count += 1

    return count / n_trials


def main():
    # ===== 参数设置 =====
    a, b, c = 3.0, 4.0, 5.0   # 三角形三边
    d = 6.0                      # 平行线间距 (需大于 max(a,b,c))
    n_trials = 1_000_000         # 模拟次数

    perimeter = a + b + c
    theoretical = perimeter / (math.pi * d)

    print("=" * 55)
    print("  Buffon 三角形问题 —— 蒙特卡洛模拟")
    print("=" * 55)
    print(f"  三角形边长: a={a}, b={b}, c={c}")
    print(f"  周长 L = {perimeter}")
    print(f"  平行线间距 d = {d}")
    print(f"  模拟次数 N = {n_trials:,}")
    print("-" * 55)

    estimated = simulate(a, b, c, d, n_trials, seed=42)

    print(f"  理论概率 P = L/(πd) = {perimeter}/(π×{d}) = {theoretical:.6f}")
    print(f"  模拟概率                 = {estimated:.6f}")
    print(f"  相对误差                 = {abs(estimated - theoretical) / theoretical * 100:.2f}%")
    print("=" * 55)


if __name__ == "__main__":
    main()
