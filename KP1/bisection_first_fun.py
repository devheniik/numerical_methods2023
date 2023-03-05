import math

print("Вкажiть 1 точку: ", end="")
ax = float(input())
print("Вкажiть 2 точку: ", end="")
bx = float(input())
print("Яка точнiсть: ", end="")
t = float(input())


def fx(x):
    global y
    y = (math.log(x) ** 2) - (0.75 * math.log(x)) + 0.125


dd = 0
cx = (ax + bx) / 2
y = 0
ay = 0
by = 0
fx(cx)
cy = y

while abs(cy) > t:
    fx(ax)
    ay = y
    fx(bx)
    by = y
    fx(cx)
    cy = y
    if ay * cy > 0:
        ax = cx
        cx = (ax + bx) / 2
    else:
        bx = cx
        cx = (ax + bx) / 2
    dd += 1

print()
print(f"Корiнь: {cx}")
print(f"Кiлькiсть крокiв: {dd}")
