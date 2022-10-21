"""5.	Дан словарь
{‘gold’: 500, ‘pouch’: [‘flint’, ‘twine’, ‘gemstone’], ‘backpack’: [‘xylophone’, ‘dagger’, ‘bedroll’, ‘bread loaf’]}.
Добавьте в словарь еще один элемент ‘pocket’, содержащий следующие значения: ‘seashell’, ‘strange berry’, ‘lint’.
Отсортируйте значения, принадлежащие ключу ‘backpack’ и затем удалите из них значение ‘dagger’.
Увеличьте  на 50 значение, принадлежащее ключу ‘gold’."""

dict1 = {'gold': 500,
         'pouch': ['flint', 'twine', 'gemstone'],
         'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']}

dict1['pocket'] = ['seashell', 'strange berry', 'lint']
dict1['backpack'] = sorted(dict1['backpack'])
dict1['backpack'] = dict1['backpack'].remove('dagger')
dict1['gold'] += 50

print(dict1)
