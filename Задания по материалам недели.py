# Задача№1 Вычисление площади треугольника ао формуле Герона
'''a = int(input())
b = int(input())
c = int(input())
p = (a+b+c)/2
S = (p*((p-a)*(p-b)*(p-c)))**0.5
print(S)'''

# Задание 2
# Напишите программу, принимающую на вход целое число, которая выводит True,
# если переданное значение попадает в интервал(−15,12]∪(14,17)∪[19,+∞) и
# False в противном случае (регистр символов имеет значение).
'''a = int(input())
if -15 < a <= 12 or 14 < a < 17 or 19 <= a:
    print(True)
else:
    print(False)'''

# Калькулятор
'''a = float(input())
b = float(input())
c = input()
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == 'mod':
      if b == 0:
       print("Деление на 0!")
      else:
       print(a % b)
if c == 'pow':
    print(a ** b)
elif c == 'div':
       if b==0:
            print("Деление на 0!")
       else:
            print(a // b)
elif c == '/':
        if b == 0:
           print("Деление на 0!")
        else:
            print(a / b)'''

# Площадь комнат
'''K = input()
if K=='прямоугольник':
 a = int(input())
 b = int(input())
 print(float(a * b))
elif K=='круг':
  r = int(input())
  print(3.14 * r ** 2)
elif K=='треугольник':
 a = int(input())
 b = int(input())
 c = int(input())
 p = (a + b + c) / 2
 S = (p * ((p - a) * (p - b) * (p - c))) ** 0.5
 print(S)'''

# Вывести максимальное, минимальное и оставшееся число
'''a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
elif c >= a and c >= b:
    print(c)
if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
elif c <= a and c <= b:
    print(c)
if a <= b and a >= c or a <= c and a >= b:
    print(a)
elif b <= a and b >= c or b >= a and b <= c:
    print(b)
elif c <= a and c >= b or c <= b and c >= a:
    print(c)'''

# Считаем программистов в комнате
'''a = int(input())
b = a % 10
c = a % 100
if b == 1 and c != 11:
    print(a, 'программист')
elif 2 <= b <= 4 and c != 12 and c != 13 and c != 14:
    print(a, 'программиста')
else:
    print(a, 'программистов')'''

# Счастливый билет
'''a = int(input())
b = a % 10
c = ((a % 100) - b) / 10
d = ((a % 1000) - (10 * c + b)) / 100
e=((a%10000)-(100*d+10*c+b))/1000
f= ((a%100000)-(1000*e+100*d+10*c+b))/10000
g=(a-(10000*f+1000*e+100*d+10*c+b))/100000
k1=b+c+d
k2=e+f+g
if k1==k2:
    print("Счастливый")
else:
    print("Обычный")'''

# 2 вариант решения
'''a, b, c, d, e, f = input()
k1 = int(a) + int(b) + int(c)
k2 = int(d) + int(e) + int(f)
if k1 == k2:
    print("Счастливый")
else:
    print("Обычный")'''
