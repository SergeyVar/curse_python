# print(12345, end='')  # Вернуть курсор на строку и продолжить печать
# print('  ', 54321)
#
## Нахождение суммы чисел в указанном диапазоне
# s = 0                       # Обязательно 0 что бы первое i прибавлялось к 0
# for i in range(1, 101):     # цикл в котором складываются все числа от 0 до 100
#    s += i                  # Переменная s меняет своё значение на i каждую итерацию цикла
# print(s)                    # После выхода из цикла выводим s
#
## Вывести пять строчек 0 ю Каждую строчку пронумеровать
# n=6
# for i in range(1,6):     # Цикл который повторяет вложенный цикл
#    print()
#    print(i,end='')
#    for j in range(n):   # Цикл выводит строчку из пяти 0
#        print(' ','0',end=' '

# Таблица умножения
#a, b, c, d = int(input()), int(input()), int(input()), int(input())  # Ввод чисел
#for i in range(c, d):  # Первый цикл выводит строку выполнив отступ
#    print('\t', i, end=' ')
#print()
#for j in range(a, b):  # Второй цикл выводит a и включает вложенный цикл
#    print()
#    print(j, end='')
#    for i in range(c, d):  # Вложенный цикл выводит произведение
#        print('\t', i * j, end='')
