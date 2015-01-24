a_list = list('abzcd')
print(a_list)

a_list.index('z')
del a_list[2]
print(a_list)

a_string = "Hello John"

# checks to see if the string is empty or not
if a_string:
	print("The string is: {} ".format(a_string))
else:
	print("The list is empty")		 

my_list = [1, 2, 3, 1]
my_list.remove(1)
# only removes the first "1"
print(my_list)
my_list.remove(1)
print(my_list)
