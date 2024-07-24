# Дополнительное практическое задание по модулю: "Основные операторы"
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
# Задание "Слишком древний шифр":

n = int(input('введите число от 3 до 20: '))

result = ''
result_list = []

for i in range(1, n // 2 +1):
    for j in range(1, n):
        if n % (i + j) == 0  and i != j and str(j) + ','  + str(i) not in result_list:
            result_list.append(str(i)+ ',' + str(j))

result_list = [i.replace(',','') for i in result_list]
result = result_list
# result= ''.join(result_list)
# result = result.replace(',','')
print('Пароль для n числа: ', *result)







