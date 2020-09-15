# Пустой список
lists=[]
# Добавляет элемент в конец списка.Можно добавлять элементы в список
lists.append('port 12')
print(lists)
lists.append('port 10')
print(lists)
# Добавляет элемент по индексу
lists.insert(0,'port1')
print(lists)
# Удаляет елемент из списка по индексу
del lists[2]
print(lists)
# Удаляет элемент из конца списка и сохраняет его в переменную
port=lists.pop()
print(lists)
print(port)
# Удаляет элемент по имени
lists.remove('port1')
print(lists)
