"""
Вычислить факториал числа N.
N! = 1 * 2 * 3 * …. * N

-----------------
Тестовые значения:
N       N!
4       24
5       120
8       40320
"""
N = 8
f = 1

for i in range(1, N+1):
    f *= i
print(f)
