#Conditional

#Q1. Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# age = input("Enter the age of pertion : ")
age = 10
age_in_int = int(age)

if age_in_int < 13:
    msg = "Child"
elif age_in_int < 20:
    msg = "Teenager"
elif age_in_int < 60:
    msg = "Adult"
elif age_in_int > 60:
    msg = "Senior"

print(msg)

#Q2 Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

# age_q2 = int(input("Enter the age : "))
age_q2 = 10
# day = input("Enter the day : ").lower()
day = "wednesday"


if age_q2 <= 18:
    tickets_price = 8
else:
    tickets_price = 12

if day == "wednesday":
    tickets_price -= 2

print("Tickets price for you is $",tickets_price)

#Q3 Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

#score = int(input("Enter your score : "))
score = 99

if score > 100:
    print("Invailid input")
elif score > 90:
    print("Grade: A")
elif score > 80:
    print("Grade: B") 
elif score > 70:
    print("Grade: C") 
elif score > 60:
    print("Grade: D") 
else:
    print("Grade: F") 

#Q4 Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe) 

fruit = "banana"
# fruit_color = input("Enter fruit color:")
fruit_color  = "green"

if fruit == "banana" and fruit_color == "green":
    print("Unripe")
elif fruit == "banana" and fruit_color == "yellow":
    print("Ripe")
elif fruit == "banana" and fruit_color == "brown":
    print("Overripe")

#Q5 Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

# weather = input("Enter weathenr condition of your city :")
weather = "sunny"
if weather == "sunny":
    print("Go for a walk")
elif weather == "rainy":
    print("Read a book")
elif weather == "sowy":
    print("Build a snowman")

#Q6 Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

# distence = int(input("Enter distence: "))
distence =  10
if distence < 3:
    transportation = "Walk"
elif distence < 15:
    transportation = "Bike"
else:
    transportation = "Car"
print(transportation)

#Q7 Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order: ", coffee)

#Q8 Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

# password = input("Enter your password: ")
password = "Password"
pass_len = len(password)

if pass_len < 6:
    print("You password is strength Weak")
elif pass_len < 10:
    print("You password is strength Medium")
else:
    print("You password is strength Strong")

#Q9 Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400)

# year = int(input("Enter Year: )"))
year = 2024

if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Normal Year")

#Q10 Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

# pet = input("Enter any one Gog and Cat :").lower()
pet = "cat"
# pet_age = int(input("Enter pet age : "))
pet_age = 3

if pet == "cat" and pet_age < 5:
    print("Senior cat food")
elif pet == "dog" and pet_age < 2:
    print("Puppy food")
else:
    print("I don't know Dear")