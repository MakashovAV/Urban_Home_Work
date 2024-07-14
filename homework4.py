# Практическая работа по уроку "Организация программ и методы строк."
# Цель: Написать программу на языке Python с использованием Pycharm для работы с методами строк и организации программ.

# 2
my_string = input("Введите строку: ")
print('Длина строки: ', len(my_string))

# 3

print(my_string.upper())
print(my_string.lower())
my_string = my_string.replace(' ', '')
print('Введенная строка без пробелов: ', my_string)

print('Первый символ строки: ', my_string[0])
print('Последний символ строки: ', my_string[-1:])
