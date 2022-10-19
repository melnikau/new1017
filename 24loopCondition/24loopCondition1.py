"""
Вывести на экран значения функции	y = (e^sin(x)) * cos()
на отрезке [0, П] с шагом 0.1.

---------------------
Тестовые значения:
0       1
0.1     1.099
0.2     1.195
3.1     -1.041
"""
import math

x = 0
y = (math.e ** (math.sin(x))) * math.cos(x)

while x <= math.pi:
    y = (math.e ** (math.sin(x))) * math.cos(x)
    print(round(x, 2), round(y, 3))
    x += 0.1
