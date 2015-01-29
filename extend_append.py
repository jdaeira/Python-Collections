letters = ['a', 'b']
letters.extend(['c', 'd'])
print(letters)

letters.append(['e', 'f'])
print(letters)

names = ['Foo', 'Bar']
names.append('Baz')
print(names)

names.extend('Moo')
print(names)

numbers = [1, 2, 3, 4, 5]
numbers.extend([6, 7])
print(numbers)

numbers.append([8, 9])
print(numbers)
