# заданное число которое будет выводиться в цикле
# каждый раз уменьшаясь на какое либо число в данном случае 1
# пока не станет равным 0
'''a = 5
# цикл while(пока выполняется условие) и само условие
while a>=0:
# Выполняемое действие
    print(a, end=' ')
# a меняет своё значение при каждой итерации цикла
    a -=1
# Получим:5 4 3 2 1 0'''
# Можно реализовать ввод числа пользователем a=int(input())

'''#Вывод всех нечётных чисел  от 5 до 55
a=5 #Начальное число
while a<56: #условие выполнения цикла
    if a%2!=0: #проверка на нечётность
       print(a, end=' ')# Выводим в одну строку через пробел
    a +=1 # каждую итерацию цикла увеличиваем переменную а на 1
# Получим:5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55'''

'''#Выводим чётные
a=5
while a<=55:
    if a%2==0:
        print(a, end=' ')
    a +=1'''

'''n=int(input()) #Произвольное число
stars = '*' # Присваеваем переменной символьное значение '*'
while len(stars) <n: #Цикл с условием длина строки(len) меньше вводимого числа
    print(stars)
    stars = stars + '*'# Каждый раз увеличиваем строку на одну'*'
#Получим:
*
**
***
****
*****'''

'''# Тоже самое только не через конкатенацию, а через умножение
n=int(input())
c=1
while c<=n:
    print('*'*c)
    c +=1'''

'''a = int(input())
b = int(input())
sum = 0
if a < b:
    while a <= b:
        sum += a
        a += 1
        print(sum)
else:
    while a >= b:
        sum += a
        a -= 1
        print(sum)'''

# Напишите программу, которая считывает со стандартного ввода целые числа,
# по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.
'''a=int(input())
s=a
if a==0:
    print(s)
else:
    while a !=0:
        a=int(input())
        s +=a
    if a==0:
        print(s)'''
'''# Нахождение НОК
a = int(input())
b = int(input())
c = 1
while True:
    if c % a == 0 and c % b == 0:
     print(c)
     break
    else:
        c +=1'''

'''while True:  #Реализован бесконечный цикл ввода
    a = int(input())
    if a < 10:
        continue
    elif a > 100:
        break
    print(a)'''
#Цикл for
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(c, d + 1):
    print('\t', i, end='')
print()
for j in range(a, b + 1):
    print(j, end='')
    for i in range(c, d + 1):
        print('\t', i * j, end='')
    print()
