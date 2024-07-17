# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
# Цель: применить навыки создания условных конструкций и знания операторов if, else, elif / and, or, not.

# Задача "Все ли равны?":

first = int(input('Введите первое число:'))
second = int(input('Введите второе число:'))
third = int(input('Введите третье  число:'))

if first == second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print('0')
