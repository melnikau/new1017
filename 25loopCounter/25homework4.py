"""4.	Дана последовательность целых чисел. Найти наименьшее число среди положительных элементов последовательности.
Если присутствует несколько одинаковых наименьших элементов, то определить их количество."""

stack = [-7, -5, -10, -54, -1, -77, -19, 72, 17, 4, 29, 14, 4, 44]
min_el = 0
counter = 0
for el in stack:
    if el > 0:
        if counter ==0:
            min_el = el
            counter += 1
        elif el < min_el:
            min_el = el
        elif el == min_el:
            counter += 1

if counter == 0:
    print("No positive numbers")
else:
    print('Min:', min_el, ',', 'quantity:', counter)
