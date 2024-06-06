#List 
my_list = ['one', 'two', 'three', 'four', 'five']
print(my_list)
print(len(my_list))

#A list with strings, integers and boolean values:
#Since lists are indexed, lists can have items with the same value:

my_list1 = ["abc", 34, True, 40, 40, "male"]
print(my_list1)
print(type(my_list1))

print('--------------')

print(my_list[0])
print(my_list[1])
print(my_list[2])

print('--------------')

print(my_list[0:3])
print(my_list[3:])
print(my_list[:3])
print(my_list[-3:-1])
print(my_list[-3:])

print('--------------')

my_list2 = [1, 2, 3, 4, 5, 6, 7]

my_list2[5] = "six"
print(my_list2)

my_list2[1:4] = ['two', 'three', 'four']
print(my_list2)

my_list2[1:3] = ['same']
print(my_list2)

my_list2.insert(7, 'Eight')
print(my_list2)


print('--------------')

# Add List Items

my_list3 = [101, 102, 103, 104, 105, 106, 107]
print(my_list3)

my_list3.append(int(108))
print(my_list3)

my_list3.extend(my_list)
print(my_list3)

print('--------------')

# Add elements of a tuple to a list:

my_tuple = ('T1', 'T2', "T3", "T4")
my_list3.extend(my_tuple)
print(my_list3)

print('--------------')

# Remove List Items

my_list4 = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', "R10"]
print(my_list4)

my_list4.remove("R1")
print(my_list4)

my_list4.pop()
print(my_list4)

my_list4.pop(1)
print(my_list4)

del my_list4[0]
print(my_list4)

# Clear the list content:
my_list4.clear()
print(my_list4)

# Delete the entire list:
# del my_list4 
# print(my_list4)

print('--------------')

# List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits)
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#Another...
newlist1 = [x for x in fruits if "a" in x]
print(newlist1)

print('--------------')

# Sort Lists

my_list5 = [5, 10, 2, 7, 1, 3, 4, 9, 8, 6]
print(my_list5)

my_list5.sort()
print(my_list5)

print('--------------')

# Make a copy of a list with the copy() method:

my_list6 = my_list5.copy()
print(my_list6)

# Make a copy of a list with the list() method:

my_list7 = list(my_list5)
print(my_list7)

print('--------------')

#  Join Lists

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)

# for x in list2:
#   list1.append(x)
# print(list1)

list3 = list1 + list2
print(list3)






