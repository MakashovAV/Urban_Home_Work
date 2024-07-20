n= 12
result = []
divider =[]
for i in range(3, n+1):
    print(i)
    if n % i == 0:
        divider.append(i)
print(divider)

for i in range(1, n //2):
    for j in range(1, n):
        for k in divider:
            if i + j == k and i != j:
                result.append([i,j])

                
print(result)

# 13 14 19 119 23 28 218 37 317 46 416 515 614 713 812 911
                
