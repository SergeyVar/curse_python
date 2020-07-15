'''a, b, c, d, e, f = input()
k1 = int(a) + int(b) + int(c)
k2 = int(d) + int(e) + int(f)
if k1 == k2:
    print("Счастливый")
else:
    print("Обычный")'''

'''a = 3
while a < 31:
    print(a, end=' ')
    a = a + 3'''

# Имя  и пароль
'''name=input('Введите ваше имя:\n')
k=3
if name == 'Сергей':
    password = input('Введите пароль:\n')
    if password=='1234':
        print('Вход выполнен успешно')
    else:
        while k>1:
            input('Введите пароль\n')
            k=k-1
        if k==1:
            print('Пароль не верен')
else:
    while k > 1:
        input('Введите ваше имя:\n')
        k = k - 1
    if k == 1:
        print('Пользователя с таким именем не существует')'''

name='Sergey'
age=48
print('Возраст {0} {1} лет'.format(name,age))


