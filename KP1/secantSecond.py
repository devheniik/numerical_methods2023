from typing import Callable
import math


def SecantMethod(f: Callable[[float], float], x0: float, x1: float, pog: float) -> float:
    f0 = f(x0)
    f1 = f(x1)
    raz = 1

    while abs(raz) > pog:
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        f2 = f(x2)

        raz = x2 - x1
        x0 = x1
        f0 = f1
        x1 = x2
        f1 = f2

    return x1


x0 = float(input("Вкажiть 1 точку: "))
x1 = float(input("Вкажiть 2 точку: "))
pog = float(input("Яка точнiсть: "))

root = SecantMethod(lambda x: (math.log(x) ** 2) - math.log(x) + 0.25, x0, x1, pog)
print(f"Корiнь: {root}")
