ast = 'астеник';norma = 'нормастеник';hyper = 'гиперстеник'
gender = input('Укажите ваш пол :').lower()
name = input('Введите своё имя:').title()
old = int(input('Ваш возраст:'))
growth = int(input('Ваш рост:'))
weight = int(input('Ваш вес:'))
wrist = int(input('Укажите обхват запястья в сантиметрах:'))
print(name, ' вы  ', end='')
if old<40:
    if gender=='женский' and wrist<15 or gender=='мужской' and wrist<18:
        print(ast)
        weight1 = (growth - 110) - ((growth - 110) / 100) * 10
        print('Ваш вес должен быть', weight1, ' kg')
    elif gender == 'женский' and  15<=wrist<=17 or gender == 'мужской' and 18<=wrist<=20:
        print(norma)
        weight1 = growth - 110
        print('Ваш вес должен быть', weight1, ' kg')
    elif gender == 'женский' and wrist>17 or gender == 'мужской' and wrist>20:
        print(hyper)
        weight1 = (growth - 110) + ((growth - 110) / 100) * 10
        print('Ваш вес должен быть', weight1, ' kg')
elif old>=40:
    if gender=='женский' and wrist<15 or gender=='мужской' and wrist<18:
        print(ast)
        weight1 = (growth - 100) - ((growth - 100) / 100) * 10
        print('Ваш вес должен быть', weight1, ' kg')
    elif gender == 'женский' and  15<=wrist<=17 or gender == 'мужской' and 18<=wrist<=20:
        print(norma)
        weight1 = growth - 100
        print('Ваш вес должен быть', weight1, ' kg')
    elif gender == 'женский' and wrist>17 or gender == 'мужской' and wrist>20:
        print(hyper)
        weight1 = (growth - 100) + ((growth - 100) / 100) * 10
        print('Ваш вес должен быть', weight1, ' kg')
if weight1 < weight:
    print('Ваш вес больше положенного на', weight - weight1, 'kg')
    print('Больше двигайтесь и меньше еште сладкого и мучного')
if weight1 >= weight:
    print('Ваш вес меньше положенного на', weight1 - weight, 'kg')
    print('Вы в прекрасной форме.Можете себе ни в чём не отказывать')