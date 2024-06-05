print("Namaste World")

# variable in python 

my_name = "Ashish"
my_roll = 58
my_clg_fee = 28000.50

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

print(my_name, my_roll, my_clg_fee)
print(type(my_name), type(my_roll), type(my_clg_fee))

a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)

# data types in python

#Str
my_string = 'Hello World'
print(my_string)
print(type(my_string), 'Immutable')
print(my_string[6])

#Int
my_integer = 999
print(my_integer)
print(type(my_integer), 'Immutable')

#Float
my_float = 99.34
print(my_float)
print(type(my_float), 'Immutable')

#Complex num
my_complex_num = 1j
print(my_complex_num)
print(type(my_complex_num))

#List
my_list = ["apple", "banana", "cherry"]
print(my_list)
print(my_list[0])
print(my_list[1])
print(type(my_list), 'Mutable')

#Tuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
print(my_tuple[0])
print(type(my_tuple), 'Immutable')

#Dictionary
my_dict = {"name" : "Atul", "age" : 150}
print(my_dict)
print(my_dict["name"])
print(my_dict["age"])
print(type(my_dict), 'Mutable')
my_dict["name"] = "Ashish"
print(my_dict)
print(my_dict["name"])


