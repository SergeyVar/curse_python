user_1 = ['Петров', 'Николай', '1978']
user_2 = ['Николаева', 'Ольга', '!983']
user_3= ['Сёмин', 'Константин', '1965']
user_4 = ['Гард', 'Николай', '1990']
dyrectory =[user_1,user_2,user_3,user_4]
len_dyrectory=len(dyrectory)
user_5=[]
x=input('Фамилия:').title()
for i in range(len_dyrectory):
    if x== dyrectory[i][0]:
        print(' Пользователь с  фамилией',x ,'существует в нашей базе,''\n','Хотите получить информацию о нём?')
        admin = input().title()
        if admin=='Да':
            print(*dyrectory[i])
        if admin == 'Нет':
            x=input('Фамилия:').title()
for i in range(len_dyrectory):
    if  x!= dyrectory[i][0]:
        print(' Пользователь с  фамилией',x ,'не существует в нашей базе,''\n','Хотите добавить информацию о нём в базу?')
        admin = input().title()
        if admin == 'Да':
            name_1=input('Фамилия:')
            user_5.append(name_1)
            name_2=input('Имя:')
            user_5.append(name_2)
            birth=input('Год рождения:')
            user_5.append(birth)
            print(user_5)
        if admin == 'Нет':
            print('Программа завершит свою работу')
            input()
            exit()





