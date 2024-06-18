#Q1 Write a function to calculate and return the square of a number.
def squre(item):
    return item ** 2

result = squre(20)
print(result)

#Q2 Create a function that takes two numbers as parameters and returns their sum.

def sumFn(num1, num2):
    return num1 + num2

print(sumFn(2, 3))

#Q3  Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(a, b):
    return a * b

print(multiply('a', 3))
print(multiply(9, 3))

#Q4 Create a function that returns both the area and circumference of a circle given its radius.

import math
def cal_cer_area(radius):
    area = round((math.pi * (radius ** 2)), 3)
    circumference = round((2* math.pi * radius) , 3)
    return area, circumference

a, b = cal_cer_area(3)
print(a)
print(b)

#Q5 Write a function that greets a user. If no name is provided, it should greet with a default name.

def greeting(name = 'Vinod...'):
    print("Hello " + name + "...!")
name = input("Enter your name : ")
greeting(name)
greeting()

#Q6 Create a lambda function to compute the cube of a number.

cube = lambda x : x**3
print(cube(2))

print('--------')

#Q7 Write a function that takes variable number of arguments and returns their sum.

def sum_of_all(*args):
    for i in args:
        print(i * 2)
    print('-----')
    return sum(args)

print(sum_of_all(1, 2, 3, 4))

#Q8 Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")

#Q9 Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i



for num in even_generator(10):
    print(num)


#Q10 Create a recursive function to calculate the factorial of a number.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))