"""
Написать программу решения квадратного уравнения
ax2 + bx + c = 0

Исходные данные: a, b, c
Результат: корни квадратного уравнения x1 и x2 или сообщение о том, что корней нет.

___________________
Тестовые значения:
a   b   c       x1      x2
2   4   10      корней нет
4   10  5       -0.69   -1.81
1  -14 15       12.83   1.17
"""
import math

a = 4
b = 10
c = 5

d = b**2 - 4*a*c

if d >= 0:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print('Корни: ', round(x1, 2), round(x2, 2))
else:
    print('Корней нет')
