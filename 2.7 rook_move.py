# coding=utf-8 Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски,
# определите, может ли ладья попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа
# от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.

a1 = int(input())
b1 = int(input())

a2 = int(input())
b2 = int(input())

if a1 == a2 or b1 == b2: print('YES')
else: print('NO')