# X = int(input())
# Y= X//60 # часы без остатка минут
# Z=X-Y*60
# print(Y)
# print(Z)

# X =int (input())
# Y = X // 60
# Z = X % 60
# print(X, '\n', Y)

# X = int(input())  # вводим минуты  до звонка будильника
# H = int(input())  # вводим часы когда легли спать
# M = int(input())  # вводим минуты когда легли спать
# h = X // 60  # переводим минуты в часы без минут
# m = X - h * 60  # остаток минут
# h1 = (M + m) // 60  # вычленяем часы из минут
# H = H + h + h1  # получаемые часы
# M = (M + m) - (h1 * 60)  # получаемые минуты
# print(H)
# print(M)

# X = int(input())
# H = int(input())
# M = int(input())
# M = X + H * 60 + M           # приобразовываем всё в минуты
# H = M//60                    # из полученного получаем часы
# M = M - H*60                 # получаем оставшиеся минуты
# print(H)
# print(M)

# amount = int(input())
# barrel = 65 l
# platform = 6 barrel
# How many platforms are needed ?
# How many empty seats are left on the platform ?

# a = int(input())
# b = a // 65
# p = b // 6
# l = a - 65 * b
# s = ((a-l)/65-(6*p))
# print(l)
# print(p)
# print(s)


#x1, x2, x3 = False, True, False
#print(not x1 or x2 and  x3)
#Приоритет no, and, or

# ((a and b) or ((not a) and (not b)))

#x=5
#y=10
#print(y > x * x or y >= 2 * x and x < y)

#a = True
#b = False
#print(a and b or not a and not b)   #

