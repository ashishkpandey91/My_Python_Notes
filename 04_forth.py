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








