l1 = ['камень', 'ножницы', 'бумага']
l2 = ['камень', 'ножницы', 'бумага']
v1 = 0  # Кол-во побед 1 игрока
v2 = 0  # Кол-во побед 2 игрока
n = 0  # Кол-во ничьих
t = int(input('Сколько партий вы хотите сыграть?:'))
for i in range(t):
    import random

    a = random.choice(l1)
    b = random.choice(l2)
    i += 1
    print(i, 'игра ', end='')
    input()
    print(a, end=' - ')
    print(b)
    if a == b:
        print('Ничья')
        n += 1
    if a == l1[0] and b == l2[1] or a == l1[1] and b == l2[2] or a == l1[2] and b == l2[0]:
        c = 'Победил первый игрок'
        print(c)
        v1 += 1
    if a == l1[1] and b == l2[2] or a == l1[2] and b == l2[1] or a == l1[0] and b == l2[2]:
        c = 'Победил второй игрок'
        print(c)
        v2 += 1
print('Статистика:')
if v1 == v2:
    n = round((n / t) * 100, 1)
    print(n, '% ничьих')
    print('У первого и второго игрока по:', (100 - n) // 2, '% побед')
if v1 > v2:
    g = round((v1 / t) * 100, 1)
    print('У первого игрока', g, '% побед')
    n = round((n / t) * 100, 1)
    print(n, '% ничьих')
    print('У второго игрока', round(100 - (g + n), 1), '% побед')
if v2 > v1:
    g = round((v2 / t) * 100, 1)
    print('У второго игрока', g, '% побед')
    n = round((n / t) * 100, 1)
    print(n, '% ничьих')
    print('У первого игрока', round(100 - (g + n), 1), '% побед')
