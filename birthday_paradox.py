#!/usr/bin/env python3
"""
生日悖论验证脚本
计算在n个人中至少有两个人生日相同的概率
"""

from math import prod

def birthday_probability(n: int, days: int = 365) -> float:
    """
    计算n个人中至少有两个人生日相同的概率

    Args:
        n: 人数
        days: 一年的天数，默认365

    Returns:
        至少两人同生日的概率
    """
    if n > days:
        return 1.0

    # 计算没有人同生日的概率: (365)*(364)*...*(365-n+1) / 365^n
    no_same_birthday = prod(days - i for i in range(n)) / (days ** n)

    # 至少两人同生日 = 1 - 没有人同生日
    return 1 - no_same_birthday


def main():
    print("生日悖论验证\n" + "=" * 50)
    print(f"{'人数':<8} {'至少两人同生日概率':<20}")
    print("-" * 50)

    # 计算1到30人的概率
    for n in range(1, 31):
        prob = birthday_probability(n)
        print(f"{n:<8} {prob*100:>18.2f}%")

    print("\n" + "=" * 50)
    print("关键节点:")
    for n in [10, 20, 23, 30, 40, 50, 60]:
        prob = birthday_probability(n)
        print(f"  {n:2d} 人: {prob*100:6.2f}%")

    # 找到超过50%的最小人数
    for n in range(1, 366):
        if birthday_probability(n) > 0.5:
            print(f"\n  → 首次超过50%: {n} 人")
            break

    # 找到超过99%的最小人数
    for n in range(1, 366):
        if birthday_probability(n) > 0.99:
            print(f"  → 首次超过99%: {n} 人")
            break


if __name__ == "__main__":
    main()
