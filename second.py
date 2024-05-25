#Numbers

#convert integer to float 

my_salary_in_int = int(34000)
print(type(my_salary_in_int), my_salary_in_int)

my_salary_in_float = float(my_salary_in_int)
print(type(my_salary_in_float), my_salary_in_float)

my_salary_in_str = str(my_salary_in_int)
print(type(my_salary_in_str), my_salary_in_str)

#similarly for others dataTypes

import random

print(random.random())

# Example 1: Random number between 0 and 9 (inclusive of 0, exclusive of 10)
print(random.randrange(10))  # Possible outputs: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# Example 2: Random number between 5 and 9 (inclusive of 5, exclusive of 10)
print(random.randrange(5, 10))  # Possible outputs: 5, 6, 7, 8, 9

# Example 3: Random number between 1 and 9 with step 2
print(random.randrange(1, 10, 2))  # Possible outputs: 1, 3, 5, 7, 9

print(random.randint(1, 20))

test = ['win', 'lose', 'draw']
print(random.choice(test))
print(random.choices(test, k=2))

my_nums = ['one', 'two', 'three', "four", 'five']
random.shuffle(my_nums)
print(my_nums)





