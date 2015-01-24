list_1 = list(range(10))
list_2 = list([10, 11, 12])
list_3 = list_1 + list_2
print(list_3)

list_3.extend(range(13, 21))

print(list_3)

alpha = list('acdf')
print(alpha)
alpha.insert(1, 'b')
print(alpha)

alpha.insert(4, 'e')
print(alpha)