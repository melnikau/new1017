"""2.	Дано натуральное число N. Определить, является ли оно простым."""

N = 21

i = 1
counter = 0

while i <= N:
    if N % i == 0:
        counter += 1
    i += 1

if counter == 2:
    print("Prostoe")
else:
    print('Ne prostoe')