"""Дано два словаря: {‘Ten’: 10, ‘Twenty’: 20, ‘Thirty’: 30} и {‘Thirty’: 30, ‘Fourty’: 40, ‘Fifty’: 50}. Объедините эти словари в один."""

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)

print(dict1)

"""

Почему не работает: 

dict_res = dict1.update(dict2)

print(dict_res) #None

"""