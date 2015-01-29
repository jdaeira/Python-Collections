my_string = "Hello there"
new_string = my_string[1:5]
print(new_string)

my_list = list(range(1,6))
print("My list is: {} ".format(my_list)) 

# This will get the last item of the list
new_list = my_list[2:len(my_list)]
print(new_list)

beginning = my_list[:3]
print(beginning)

end = my_list[0:]
print(end)

all_list = my_list[:]
print(all_list)

print(my_list)

num_list = [5, 3, 2, 1, 7]
num_list.sort()
print(num_list)

range_list = list(range(20))
print(range_list)

# From the beginning to the end of the list and add 2 steps
# [start:stop:step]
even_list = range_list[::2]
print(even_list)

# To leave off the zero and one
nozero_list = range_list[2::2]
print(nozero_list)

state_string = "Oklahoma"
second = state_string[::2]
print(second)
reverse = state_string[::-1]
print(reverse)

first_four = range_list[0:4]
print(first_four)

last_four = range_list[-4:]
print(last_four)

toget = first_four + last_four
print(toget)