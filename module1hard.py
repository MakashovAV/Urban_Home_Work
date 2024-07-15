# Дополнительное практическое задание по модулю: "Базовые структуры данных."
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

abc_list_students = sorted(list(students))      # Создаем сортированный по алфавиту список учеников

GPA_grades = []
for x in range(len(grades)):
    GPA_grades.append(sum(grades[x]) / len(grades[x]))    # Создаем список среднего балла учеников

dict_GPA_students = dict(zip(abc_list_students, GPA_grades))    # Создаем необходимый словарь:  ключ - "имя ученика", значение - "средний балл"
print(dict_GPA_students)
