"""
Дан список слов: ['snow', 'rain', 'wind', 'sun', 'clouds']. Выведите на экран:
- все слова, длина которых больше 3-х символов
- все слова, расположенные до слова длиной 3 символа
"""
l = ['snow', 'rai', 'wind', 'sun', 'clouds']

for el in l:
    if len(el) <= 3:
        continue
    else:
        print(el, end=' ')
print()

for el in l:
    if len(el) == 3:
        break
    else:
        print(el, end=' ')