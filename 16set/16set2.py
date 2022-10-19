"""
Даны два списка чисел, содержащие 10 и 15 элементов соответственно.
Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания,
а все остальные - в порядке убывания.
"""

l1 = [5, 1, 2, 7, 4, 5, 6, 41, 8, 9]
l2 = [7, 6, 10, 8, 9, 5, 19, 11, 12, 13, 14, 15, 16, 17, 18]

s1 = set(l1)
s2 = set(l2)

print(s1, s2)

common_elements = s1.intersection(s2)#s1 & s2

print(common_elements)

sorted_common_elements = sorted(common_elements)
print(sorted_common_elements)

other_elements = s1.symmetric_difference(s2)#s1 ^ s2
sorted_other_elements = sorted(other_elements, reverse=True)
print(sorted_other_elements)
