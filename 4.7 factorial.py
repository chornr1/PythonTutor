# coding=utf-8
# Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
# По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.

n = int(input())
prod = 1

for i in range(1, n + 1):
    prod *= i

print(prod)
