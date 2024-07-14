# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

#2
immutable_var = (5, [555,5] , 'строка',True, (5,4), 5.5)
print(immutable_var)

# 3
print(type(immutable_var))
# immutable_var[0] = 5
# immutable_var[2] = 'asdf'
# такие операции выдают ошибку, потому что тип данных "tuple" является неизменяемым,
# и после создания кортежа мы не можем изменить, ни тип данных, ни значения хранящихся в нем элементов

# immutable_var[1] = False  # Изменить list на bool невозможно
immutable_var[1][0] = 15 # Но мы можем изменить значение сомого списка
print(type(immutable_var[1]))
print(immutable_var)

# 4
mutable_list = [5, [555,5] , 'строка',True, (5,4), 5.5]
print(mutable_list)
mutable_list[0] = 10
mutable_list[1][0] = 10
mutable_list[2] = 'новая строка'
mutable_list[3] = False
print(mutable_list)

