"""
Дана строка символов, среди которых есть одна открывающаяся и
одна закрывающаяся скобки. Вывести на экран все символы,
расположенные внутри этих скобок.
"""

s = b"Any long( text text)p"

index_open_br = s.index(b'(')
index_close_br = s.index(b')')

print(s[index_open_br+1:index_close_br])