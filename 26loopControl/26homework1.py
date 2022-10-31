"""Дан диапазон чисел от 1 до 9.
Необходимо написать программу, которая будет последовательно суммировать числа из диапазона,
пока не будет достигнута сумма, равная 15, и затем выведет на экран количество чисел, которые для этого потребовалось сложить.
Напишите два варианта решения задачи: с использованием цикла for и с использованием цикла whi1е.
"""

sum_result = 0
counter = 0
for el in range(9):
    if sum_result < 15:
        sum_result += el
        counter += 1
print(sum_result, counter)

i = 0
sum_result2 = 0
counter2 = 0
while i < 9:
    if sum_result2 >= 15:
        print(sum_result2, i)
        break
    else:
        sum_result2 += i
        i += 1
