"""
Дана строка 'Break and Continue operators'.
Выведите на экран данную строку до символа ‘p’ включительно, пропуская при этом каждый третий символ.
"""
s = 'Break and Continue operators'

for i in range(0, len(s)):
    if s[i] == 'p':
        if i % 3 == 2:
            print(s[i], end='')
        break
    if i > 0 and i % 3 == 2:
        continue
    print(s[i], end='')
