import math

import math
from typing import Tuple

print("Вкажiть 1 точку: ")
ax = float(input())
print("Вкажiть 2 точку: ")
bx = float(input())
print("Яка точнiсть: ")
t = float(input())


y = 0
yy = 0
c = 0
ay = 1
by = 1


def function_f(x):
    return (math.log(x) ** 2) - (0.75 * math.log(x)) + 0.125


def chord_method(func: callable, x1: float, x2: float, eps: float, n: int) -> float:
    while abs(x2 - x1) > 2 * eps:
        x1 = x2 - func(x2) * (x2 - x1) / (func(x2) - func(x1))
        x2 = x1 - func(x1) * (x1 - x2) / (func(x1) - func(x2))
        n += 1
    return x2



print()
print(f"Корiнь: {chord_method(function_f, ax, bx, t, 1)}")
