"""
Дана строка, содержащая русскоязычный текст.
Найти количество слов, начинающихся с буквы “е”.

"""

s = b"test one "\
    b"test two. "\
    b"tswt three "\
    b"trfy four."

count_E = s.count(b't')
count_e = s.count(b' f')
count_res = count_e + count_E
print('Count_res = ', count_res)
