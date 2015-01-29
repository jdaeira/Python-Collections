import math

my_list = [1, 2, 'a', 'b', 'c', 'd', 5, 6, 7, 'f', 'g', 'h', 8, 9, 'j']
print(my_list)

# removes the 1 and 2
del my_list[:2]
print(my_list)

# replaces 5, 6, 7 with e and f
my_list[4:7] = ['e', 'f']
print(my_list)

# removes the duplicate f
my_list.remove('f')
print(my_list)

# replaces 8 and 9 with i
my_list[8:10] = ['i']
print(my_list)

# The first half of the string, rounded with round(), should be lowercased.
# The second half should be uppercased.
# E.g. "Treehouse" should come back as "treeHOUSE"


round_up = math.ceil(4.5)
print(round_up)

round_down = math.floor(4.5)
print(round_down)


str1 = "Treehouse"
print(str1[0])
print(len(str1))
number = 5.5
print(round(number))

number = int(len(str1) / 2) 
print(number)
print(round(number))
rounded = round(number)
first_half = str1[:rounded].lower()
print(first_half)
second_half = str1[rounded:].upper()
print(second_half)
print(first_half + second_half)

lower = str1.lower()
print(lower)
upper = str1.upper()
print(upper)

def sillyCase(word):
    rounded = round(len(word) / 2)
    first_half = word[:rounded].lower()
    second_half = word[rounded:].upper()
    return first_half + second_half


silly = sillyCase("Treehouse")
print(silly)

