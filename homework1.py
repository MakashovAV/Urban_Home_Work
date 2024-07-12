#  Практическое задание по уроку "Строки и индексация строк"
#  Цель: Научиться работать со строками и индексацией строк в Python.

# 1
example = '012345678'

# 2
print(example[0])

# 3
print(example[-1])

# 4
lenght_example = len(example)                   # Получаем длину сторки
mid_example = int(lenght_example / 2)           # Вычисляем середину строки и отбрасываем остаток деления на 2
print(example[mid_example:])                    # Выводм вторую половину строки с нечётным количеством символов

# 5
print(example[::-1])                            # Выводим всю строку с отрицательным шагом
#  reversed_exaple = ''.join(reversed(example)) # Второй способ  с использованием функции reversed
#  print(reversed_exaple)

# 6
print(example[1::2])
