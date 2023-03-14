x = 1234 #пароль
z = True
while z:
    a = int(input())
    if a == x: #проверяем пароль
        print('верный пароль') 
        z = False
    else:
        print('неверный пароль')
