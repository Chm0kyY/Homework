x = 1234
z = True
while z:
    a = int(input())
    if a == x:
        print('верный пароль')
        z = False
    else:
        print('неверный пароль')
