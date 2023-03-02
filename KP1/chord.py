import math

print("Вкажiть 1 точку: ", end="")
ax = float(input())
print("Вкажiть 2 точку: ", end="")
bx = float(input())
print("Яка точнiсть: ", end="")
t = float(input())

y = 0
yy = 0
c = 0
ay = 1
by = 1


def fx(x):
    global y
    y = (math.log(x) ** 2) - (0.75 * math.log(x)) + 0.125


def fx2(x):
    global yy
    yy = (math.log(x) ** 2) - math.log(x) + 0.25


fx(ax)
fx2(ax)
if y * yy < 0:
    while abs(ay) > t:
        fx(ax)
        ay = y
        fx(bx)
        by = y
        ax = -ay * (bx - ax) / (by - ay) + ax
        c += 1
    print()
    print(f"Корiнь: {ax}")
    print(f"Кiлькiсть крокiв: {c}")
else:
    while abs(by) > t:
        fx(ax)
        ay = y
        fx(bx)
        by = y
        bx = -by * (ax - bx) / (ay - by) + bx
        c += 1
    print()
    print(f"Корiнь: {bx}")
    print(f"Кiлькiсть крокiв: {c}")
