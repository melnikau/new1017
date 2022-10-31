"""Дан список имен: ['Rose', 'Nina', 'Phillip', 'Alex', 'Jimmy', 'Max'].
Вывести на экран приветственную строку в формате ` Нello naame' для всех имен длиной не более 4-х символов.
При этом все имена, следующие за именем, содержащим букву х, должны быть проигнорированы.
"""

l = ['Rose', 'Nina', 'Phillip', 'Alex', 'Jimmy', 'Max']
for el in l:
    if 'x' in el:
        continue
    if len(el) <= 4:
        print('Hello, ', el)
