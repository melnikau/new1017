"""
Написать программу, которая будет запрашивать у пользователя пароль до тех пор,
пока он не удовлетворит следующим критериям:
- длина пароля не менее 8 символов
- пароль не содержит в себе имя пользователя
"""
name = input('name: ')
psw = input('psw: ')

while True:
    if len(psw) < 8:
        print('Too short password')
    elif name in psw:
        print('psw contains name')
    else:
        print("psw was set")
        break
    psw = input('psw: ')
