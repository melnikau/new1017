"""
Вычислить сумму натуральных четных чисел, не превышающих заданное число N.
2, 4, 6, 8, 10, ….

--------------------
Тестовые значения:

N       sum
10      30
14      56
20      110
"""
N = 20
i = 0
sum_n = 0
while i <= N:
    sum_n += i
    i += 2

print(sum_n)
