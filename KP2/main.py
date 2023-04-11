import math
from typing import Callable, Tuple


def function_f(x):
    return (math.cos(x) ** 2) + (0.5 * math.cos(x)) + (1 / 18)


def function_g(x):
    return (math.cos(x) ** 2) + ((1 / 3) * math.cos(x)) + (1 / 36)


def function_p(x):
    return x + math.log(x) - 0.5


def function_q(x):
    return (x ** 3) + (0.4 * x ** 2) + (0.6 * x) - 1.6


def bisection(func: Callable[[float], float], x1: float, x2: float, eps: float, n: int) -> Tuple[float, float]:
    mn = 0.5 * (x1 + x2)
    f_x1 = func(x1)
    f_mn = func(mn)
    n += 1

    if abs(x2 - x1) > eps:
        tmp = f_x1 * f_mn
        if tmp <= 0:
            return bisection(func, x1, mn, eps, n)
        else:
            return bisection(func, mn, x2, eps, n)
    else:
        if abs(f_mn) > eps:
            print("This function doesn`t have an answer in this range or the algorithm can`t find it.")
            return -1, -1
        else:
            return mn, (x2 - x1) / pow(2, n + 1)


def chord_method(func: Callable[[float], float], x1: float, x2: float, eps: float, n: int) -> Tuple[float, float]:

    while True:
        x1 = x2 - func(x2) * (x2 - x1) / (func(x2) - func(x1))
        x2 = x1 - func(x1) * (x1 - x2) / (func(x1) - func(x2))
        n += 1

        if abs(x2 - x1) <= 2 * eps:
            break

    return x2, (x2 - x1) / pow(2, n + 1)


def secant_method(func: Callable[[float], float], x1: float, x2: float, eps: float, n: int) -> Tuple[float, float]:
    res = 0
    x1 = x2 + 0.1

    while True:
        tmp = res
        res = x2 - func(x2) * (x2 - x1) / (func(x2) - func(x1))
        x1 = x2
        x2 = res
        n += 1

        if abs(tmp - res) <= 2 * eps:
            break

    return x2, (x2 - x1) / pow(2, n + 1)


def newton(func: Callable[[float], float], x1: float, x2: float, eps: float, n: int) -> Tuple[float, float]:
    x = x2
    alpha = 1e-9
    delta = 1

    while abs(delta) > eps:
        f_x = func(x)
        f_xa = func(x + alpha)
        df = (f_xa - f_x) / alpha
        delta = f_x / df
        x -= delta
        n += 1

        if x <= x1:
            break

    return x, (x2 - x1) / pow(2, n + 1)



def newton_simple(func: Callable[[float], float], x1: float, x2: float, eps: float, n: int) -> Tuple[float, float]:
    x = x2
    alpha = 1e-9
    delta = 1

    f_x = func(x2)
    f_xa = func(x2 + alpha)
    df = (f_xa - f_x) / alpha

    while abs(delta) > eps:
        f_x = func(x)
        delta = f_x / df
        x -= delta
        n += 1

        if x <= x1:
            break

    return x, (x2 - x1) / pow(2, n + 1)


def simple_iteration(func: Callable[[float], float], x1: float, x2: float, eps: float, n: int) -> Tuple[float, float]:
    x1 = -2
    b = 0
    y = 0

    while True:
        y = func(x1)
        b = abs(x1 - y)
        x1 = y
        n += 1

        if b < eps:
            break

    return x1, b




e1 = 1e-4
e2 = 1e-5
e3 = 1e-6
a = 0.1
b = 2

fun_number = input("Choose function \n"
                   "1 - f math.cos(x) ** 2) + (0.5 * math.cos(x)) + (1 / 18),\n"
                   "2 - g (math.cos(x) ** 2) + ((1 / 3) * math.cos(x)) + (1 / 36),\n"
                   "3 - p x + math.log(x) - 0.5, \n"
                   "4 - q (x ** 3) + (0.4 * x ** 2) + (0.6 * x) - 1.6 \n"
                   )

method = function_f

way_number = input("Choose method:\n"
                   "1 Bisection method\n"
                   "2 Chord method\n"
                   "3 Secant method\n"
                   "4 Newton method\n"
                   "5 Newton simple method\n"
                   "6 Simple Iteration Simple method\n"
                   "Your choose: ")

if fun_number == "1":
    method = function_f
elif fun_number == "2":
    method = function_g
elif fun_number == "3":
    method = function_p
elif fun_number == "4":
    method = function_q

way = bisection

if way_number == "1":
    way = bisection
elif way_number == "2":
    way = chord_method
elif way_number == "3":
    way = secant_method
elif way_number == "4":
    way = newton
elif way_number == "5":
    way = newton_simple
elif way_number == "6":
    way = simple_iteration

print(f"For 1e-4: {way(method, a, b, e1, 1)}")
print(f"For 1e-5: {way(method, a, b, e2, 1)}")
print(f"For 1e-6: {way(method, a, b, e3, 1)}")
