n= 20
result = []
divider =[]
for i in range(3, n+1):
    print(i)
    if n % i == 0:
        divider.append(i)
print(divider)

for i in range(1, n):
    for j in range(1, n):
        divider_1 = divider
        for k in divider_1:
            if i + j == k:
                result.append(str(i) + str(j))

                
print(result)
# 13 14 19 119 23 28 218 37 317 46 416 515 614 713 812 911
                
