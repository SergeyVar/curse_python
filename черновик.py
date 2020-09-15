# s='aaaabbcaa'
# k=1
# i=0
# j =i+1
# l=len(s)
# while j<l:
#    if s[i]==s[j]:
#        k +=1
#        i +=1
#        j=i+1
#        print(s[i]+str(k))


# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
# s=0
# for i in range(0,1000):
#    if i%3==0 or i%5==0:
#        s +=i
# print(s)

# 10 000 часов
# h1 = int(10000/1)
# h = h1 % 24
# y = h1 // 365
# d = h1 % 365
# m = d // 31
# d = d % 31
# if y<10:
#    y=str(y)
#    y='0'+y
# if m<10:
#    m = str(m)
#    m='0'+m
# if d<10:
#    d = str(d)
#    d='0'+d
# if h<10:
#    h = str(h)
#    h='0'+h
# print(y,m,d,h,sep=':')
# Рисуем W
# a='*'
# p=' '
#
# for i in range(1,6):
#
#    if i==1:
#        print(a+5*p+a+5*p+a)
#    if i==2:
#        print(p+a+3*p+a+p+a+3*p+a)
#    if i == 3:
#        print(2*p + a + p + a+3*p+a+p+a)
#    if i==4:
#         print(3*p+a+5*p+a)

# a,b,c=(int(i) for i in input().split())
# print((a+b+c)/3)
# print(2*(a+c)-3*b)

# Поменять местами значения двух переменных без использования третьей
# a=2
# b=17
# print(a,b)
# a,b=b,a
# print(a,b)
# Даны три переменные a, b и c. Изменить значения этих переменных так,
# чтобы в a хранилось значение a+b, в b хранилась разность старых
# значений c−a, а в c хранилось сумма старых значений a+b+c.
# a = 0
# b = 2
# c = 5
# c = a + b + c
# a = a + b
# b = (c - 2 * b) - (a - b)
# print(a, b, c)

# s='bacaaad'           # строка
# s=s.upper()           # метод  BACAAAD
# k=0                   # счётчик
# p='aa'                # подстрока
# print(s)
# s=s.lower()           # метод bacaaad
# print(s)
# for c in s:           # считаем скоько символов а в строке
#    if c=="a":
#        k +=1         # счётчик цыклов пкажет сколько а 4
# print(k)
# print(s.count(p))     # метод сольк подстрок р в строке s 1
# print(s.find(p))      # метод показывает индекс в строке кода появляется подстрока р 3
# if p in s:            # проверка сть ли подстрок р в строке s yes
#    print('yes')#
# print(s.replace('a','F')) # замена символа в строке на другой было bacaaad стало bFcFFFd
#
# s='ATTRFFFFEWET'
# print(s[0])            # A
# print(s[1:4])          # TTR
# print(s[:4])           # ATTR
# print(s[4:])           # FFFFEWET
# print(s[-4:])          # EWET
# print(s[::-1])         # TEWEFFFFRTTA
# print(s[:11:2])        # ATFFEE

# Является ли строка полиндромом
# s=input()
# i=0
# j=len(s)-1
# polindrom= True
# while i<j:
#    if s[i] != s[j]:
#        polindrom=False
#        break
#    i +=1
#    j  -=1
# if polindrom:
#    print('yes')
# else:
#    print('no')
# Более простой и короткий вариант
# s=input()
# r=s[::-1]
# if r==s:
#    print('yes')
# else:
#    print('no')

# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов
# исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.
#  Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит
#  закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

# s = input()
# i = 0
# count = 1
# out = ''
# while i< (len(s) - 1):
#    if s[i] == s[i+1]:
#        count += 1
#    else:
#        out = out + s[i] + str(count)
#        count = 1
#    i +=1
# print(out+ s[i] + str(count))

# x,y,z=1,2,3
# print(x,z,y)

a=''
while a !='end':
    a=input()
print(a)
