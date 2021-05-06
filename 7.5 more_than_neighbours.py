# coding=utf-8 Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей,
# и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно
# соседей.

L = [int(i) for i in input().split()]

count = 0
for i in range(1, len(L)-1):
    if L[i-1] < L[i] and L[i+1] < L[i]:
        count += 1

print(count)