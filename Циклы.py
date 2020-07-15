'''a = 5
while a>=0:
    print(a, end=' ')
    a -=1'''

'''a=5
while a<56:
    if a%2!=0:
       print(a, end=' ')
    a +=1'''

'''n=int(input())
stars = '*'
while len(stars) <n:
    print(stars)
    stars = stars + '*'''
'''n=int(input())
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
# Нахождение НОК
a = int(input())
b = int(input())
c = 1
while True:
    if c % a == 0 and c % b == 0:
     print(c)
     break
    else:
        c +=1

