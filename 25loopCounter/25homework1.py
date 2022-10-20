"""
1.	Вычислить сумму натуральных четных чисел, не превышающих N.
"""

N = 10

i = 0
sum_odd = 0

while i <= N:
    if i % 2 == 0:
        sum_odd += i
    i += 1
print(sum_odd)
