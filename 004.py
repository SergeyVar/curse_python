# import time
#
# for i in range(10,0,-1):
#     print(i,end='  ')
#     time.sleep(1)
# print('START')

# Таблица умножения
# for i in range(1,10):
#     for j in range(2, 10):print(j, '*', i, '=', j * i,end='     ')
#     print()

# Числа Фибоначчи
# a,b=0,1
# while b <1000:
#     print(b,end='  ')
#     a,b=b,b+a

# a = [1,2,7,123,68,456]
# for x in a[:]:
#     if x < 100: a.insert(0,x)
#
# for x in a:
#     print(x,end=' ')

# for i in range(50, 1, -5): print(i, end=' ')

# d={1:2,3:4,4:5}
# key=5
# value=4
# if key in d.keys():
#     d[key]=value
# elif key not in d.keys():
#     if 2*key in d.keys():
#         d[2*key] = value
#     else:
#         d[2*key]=value
#
# print(d)


# Вы можете использовать метод setdefault для создания списка как
# value для key , даже если этот key еще не находится в словаре .
# Так что это делает код очень простым:
# >>> d = {}
# >>> d.setdefault(1, []).append(2)
# >>> d.setdefault(1, []).append(3)
# >>> d.setdefault(5, []).append(6)
# >>> d
# {1: [2, 3], 5: [6]}


# d = {}
# def update_dictionary(d, key, value):
#     if key in d.keys():
#         d.setdefault(key, []).append(value)
#     if key not in d.keys():
#         d.setdefault(2 * key, []).append(value)


# str_1 = input().lower().split()
# m = 0
# str_2 = ''
# lst_1 = []
# for i in str_1:
#     m = str_1.count(i)
#     str_2 = i + ' ' + str(m)
#     lst_1.append(str_2)
# for i in set(lst_1):
#     print(i)

# a = 'Т**кто*'
# print('У нас есть слово', a ,'Попробуй узнать его угадав буквы скрытые за звёздочками')
# b = input('Маленькая подсказка - вторая и пследняя буквы это одна и таже буква. Угадайте её:')
# while b!='р':
#     b = input('Пока не верно. Попробуй ещё раз:')
# print('Верно это буква р')
# print('Получается','Тр*ктор')
# c = input('Это простая задача. Угадайте третью букву:')
# while c!='а':
#     c = input('Подума лучше. Третья буква это:')
# print('Верно это а')
# print('Трактор')

# Игра * УГАДАЙ СЛОВО*

import random

d = ['башня', 'торпеда', 'колокол', 'мотоцикл', 'радуга',       # База отсюда берём слово
     'виноград', 'частокол', 'лёд', 'рыбалка', 'кастрюля',
     'вилка', 'каммод', 'жираф', 'собака', 'скрипка', 'сирота', 'кинжал',
     'колонна', 'маховик', 'дирижабль', 'сапог', 'топор']
a = list(random.choice(d))  # рандомно выбираем слово из d
len_a = len(a)
b = a.copy()    # создаём тестовый список будем сверятсься с ним
lst_ind = []    # список индексов пропущенных букв
r = random.randint(0, len_a - 1) # Случайные числа (сократить код!!!)
r1 = random.randint(0, len_a - 1) # сделать только с r
r2 = random.randint(0, len_a - 1)
r3 = random.randint(0, len_a - 1)
if len_a <= 5:    # Если длина слова  < 5 - 2 пропущенных буквы
    a[r] = '*'
    a[r1] = '*'
elif len_a > 5:   # Если длина слова > 5 - 4 пропущенных буквы
    a[r] = '*'
    a[r1] = '*'
    a[r2] = '*'
    a[r3] = '*'
for i in range(len_a):    # Добавляемых индексы скрытых букв
    if a[i] == '*':
        lst_ind.append(i + 1)
print(*a)
if 1 < len(lst_ind) < 5:     # Условие для 'буквы' или 'букв'
    print('Вам нужно угодать ', len(lst_ind), ' буквы', (*lst_ind))
else:
    print('Вам нужно угодать ', len(lst_ind), ' букв', (*lst_ind))

print(*b)
