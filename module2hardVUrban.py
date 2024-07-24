n = int(input('введите число от 3 до 20: '))

result = []
for i in range(1, n+1):
    for u in range(1, n+1):
        if n % (i + u) == 0 and u>i:
            result.append(i)
            result.append(u)
result1 = ''
for p in result:
    result1 += str(p)

print('Шифр: ', result1)