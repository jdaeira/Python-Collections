names = ["Kenneth", "Joy", "Sam"]
names_list = list(["Kenneth", "Joy", "Sam"])

names_1 = names.pop()
names_2 = names.pop(0)
print(names_1)
print(names_2)
print(names)

the_list = ["a", 2, 3, 1, False, [1, 2, 3]]
the_list.insert(0, the_list.pop(3))  # the_list is now [1, "a", 2, 3, False, [1, 2, 3]]
#the_list.remove('a')
print(the_list)
del the_list[1]
print(the_list)
the_list.remove(False)
print(the_list)
the_list.remove([1, 2, 3])
print(the_list)
the_list.extend(range(4,21))
print(the_list)
