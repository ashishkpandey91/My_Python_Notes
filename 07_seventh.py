#Loops

#Q1 Given a list of numbers, count how many are positive.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count = 0
for num in numbers:
    if num > 0:
        count += 1
print(count)

#Q2 Calculate the sum of even numbers up to a given number n.

# num = int(input("Enter the number: "))
num = 10
sum = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        sum += i
print(sum)

#Q3 Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# num1 = int(input("Enter the posetive number : "))
num1 = 5

for i in range(1, 11):
    print(num1, 'x', i,'=', num1*i)

#Q4 Reverse a string using a loop.

# inputStr = input("Enter any string : ")
inputStr = "Babulal chaube sahab"
ReverseStr = ""

for char in inputStr:
    ReverseStr = char + ReverseStr
print(ReverseStr)

#Q5 Find the First Non-Repeated Character

# my_string = input("Enter any string : ")
my_string = "assatuu"

for char in my_string:
    if my_string.count(char) == 1:
        print("Char is : ", char)
        break

#Q6 Compute the factorial of a number using a while loop.

# userInput =int( input("Enter a posetive number: "))
userInput = 5

fact = 1

while userInput > 0:
    fact = fact * userInput
    userInput -= 1
print("Factorial", fact)

#Q7 Keep asking the user for input until they enter a number between 1 and 10.



while True :
    inputNum = int(input("Enter a number between 1-10 : "))
    if 0 <= inputNum <= 10 :
        print("Thanks")
        break
    
    print("invalid Input")

#Q8 Check if a number is prime.

inputInteger = int(input("Enter posetive integer :"))
# inputInteger = 25

flag = True

while inputInteger > 1:
    if inputInteger % i == 0:
        flag = False
    inputInteger -= 1
if flag == True:
    print("your given number is prime number")
else:
    print("your given number is not prime number")


#Q9 Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate detected", item)
        break
    unique_item.add(item)

#Q10 Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time
wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time, )
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
