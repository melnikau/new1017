"""2.	Дан словарь
{‘name’: ‘Alex’, ‘age’: 12, ‘class’: ‘v’, ‘roll_id’: ‘2’}.
Проверить принадлежат ли следующие значения  словарю:
‘class’, ‘Alex’, ‘Michael’, ‘4’, ‘2’, ‘age’, ‘address’, (‘name’, ‘Alex’), (‘class’, ‘x’)."""

dict = {'name': 'Alex',
        'age': 12,
        'class': 'v',
        'roll_id': '2'}

print('class as key: ', 'class' in dict.keys())
print('class as value: ', 'class' in dict.values())

print('Alex as key: ', 'Alex' in dict.keys())
print('Alex as value: ', 'Alex' in dict.values())

print('4 as key: ', '4' in dict.keys())
print('4 as value: ', '4' in dict.values())

print('2 as key: ', '2' in dict.keys())
print('2 as value: ', '2' in dict.values())

print('age as key: ', 'age' in dict.keys())
print('age as value: ', 'age' in dict.values())

print('address as key: ', 'address' in dict.keys())
print('address as value: ', 'address' in dict.values())

print('("name", "Alex") as key/value: ', ('name', 'Alex') in dict.items())

print('("class", "x") as key/value: ', ('class', 'x') in dict.items())
