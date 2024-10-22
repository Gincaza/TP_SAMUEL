import random

a = random.uniform (1, 10)
b = random.uniform (5, 10)
c = random.uniform (5, 10)

d = b ** 2 - 4 * a * c

print(f"valores: a = {a}, b = {b}, c = {c}")
print(f"delta (d) = {d}")

if d < 0:
    print("não há raiz real")
elif d == 0:
    x = -b / (2 * a)
    print(f"há uma raíz: x = {x}")
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(f"duas raizes reais: x1 = {x1}, x2 = {x2}")



