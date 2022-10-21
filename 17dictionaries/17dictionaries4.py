"""
Дан словарь {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}.
Найти 3 наибольших значения в нем.
"""

d = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
values = d.values()

sorted_values = sorted(values, reverse=True)
print(sorted_values)

print(sorted_values[0:3])