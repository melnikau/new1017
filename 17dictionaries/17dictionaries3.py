"""
Дан словарь {'data1': 100, 'data2': -54, 'data3': 247}.
Найти сумму значений словаря.
"""

d = {'data1': 100, 'data2': -54, 'data3': 247}

values = d.values()

print(values)

sum_values = sum(values)

print(sum_values)