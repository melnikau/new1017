"""
Дана строка, заканчивающаяся точкой.
Подсчитать, сколько слов в строке.
"""

s = "Дана строка, заканчивающаяся точкой."

s = s.replace(',', '')
s = s.replace('.', '')

l = s.split()
print(l)

count = len(l)
print('Count:', count)
