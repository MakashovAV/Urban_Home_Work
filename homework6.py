# Практическое задание по теме: "Словари и множества"
# Цель: Написать программу на языке Python, используя Pycharm, для работы со словарями и множествами.

# 2
my_dict = {'Андрей': 1989,
         'Вася': 1985,
         'Den': 2001,
         'Теона': 2021}
print('Словарь: ', my_dict)
print('День рождения Тео: ', my_dict['Теона'])
print('День рождения Папы: ', my_dict.get('Папа', 'Не знаю'))

my_dict.update({'Женя': 2015, 'Страик': 1952})
print('День рождения Васи: ', my_dict.pop('Вася'))
print('Словарь: ', my_dict)

# 3
my_set = {1, 1, 'set', 'Set', 'set', True, 5, 4, 4, 9.9, 9.9}
print(my_set)
my_set.update({(3, 5), 34})
my_set.remove(1)
print(my_set)