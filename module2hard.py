n = int(input('введите число от 3 до 20'))
result = ''
result_ = []
divider =[]
for i in range(3, n+1):
    if n % i == 0:
        divider.append(i)
print(divider)
if n % 2 == 0:
    x = n // 2
else:
    x = n // 2 +1

for i in range(1, x):
    for j in range(1, n):
        for k in divider:
            if i + j == k and i != j:
                result_.append([i,j])
                for x in result_:
                    if x == [j, i]:
                        result_.remove([i, j])
                        
for i in result_:
    result += (str(i[0]) + str(i[1]))
print(result)
# 13 14 19 119 23 28 218 37 317 46 416 515 614 713 812 911
                
