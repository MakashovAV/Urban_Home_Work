n = int(input('введите число от 3 до 20: '))
result = ''
result_ = []

for i in range(1, n // 2 + 1):                          # Перебираем первое число
    for j in range(1, n):                               # Перебираем второе число
        if n % (i + j) == 0 and i != j:                 # Делаем список пар
            result_.append([i, j])
            for x in result_:
                if x == [j, i]:
                    result_.remove([i, j])              # Сразу убираем "обратные" пары

for i in result_:
    result += (str(i[0]) + str(i[1]))                   # Склеиваим пары в пароль
print(result)
