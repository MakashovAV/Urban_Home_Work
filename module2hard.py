n = int(input('введите число от 3 до 20: '))
result = ''
result_ = []
divider = []
for i in range(3, n + 1):                               # Находим возможные делители
    if n % i == 0:
        divider.append(i)
if n % 2 == 0:                                          # ограничиваем перебор первого числа
    x = n // 2
else:
    x = n // 2 + 1

for i in range(1, x):                                   # Перебираем первое число
    for j in range(1, n):                               # Перебираем второе число
        for k in divider:
            if i + j == k and i != j:                   # делаем список пар
                result_.append([i, j])
                for x in result_:                       # Сразу убираем "обратные" пары
                    if x == [j, i]:
                        result_.remove([i, j])

for i in result_:
    result += (str(i[0]) + str(i[1]))                   # Склеиваим пары в пароль
print(result)
