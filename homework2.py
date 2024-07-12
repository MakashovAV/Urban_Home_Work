# Практическое задание по работе в Pycharm - "Переменные".
# Цель: научиться правильно называть переменные и взаимодействовать с ними.

homework_count = 12
homework_hours = 1.5
course_name = 'Pyton'
time_for_one_task = homework_hours / homework_count
print('Курс: ', course_name,
      ', всего задач: ', homework_count,
      ', затрачено часов: ', homework_hours,
      ', среднее время выполнения ', time_for_one_task, ' часа', sep='', end='.')


# Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

a = 'a'
b = 'b'
c = 'c'
print(a,b,c, sep = '-')

x = 15
y = 2.5
i = y / x
print("Было их: ", x, "человек.", "На всех было: ", y, "литра водки.", "Получается каждому всего по", i, "литра")