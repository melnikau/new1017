"""3.	Дана последовательность целых положительных чисел. Определить количество простых чисел в последовательности."""

stack = [7, 5, 10, 54, 77, 19, 72, 17, 29, 14, 45, 44]
counter_res = 0

for el in stack:
    counter = 0
    for i in range(1, el+1):
        if el % i == 0:
            counter += 1
    if counter == 2:
        print(el)
        counter_res += 1

print(counter_res)
