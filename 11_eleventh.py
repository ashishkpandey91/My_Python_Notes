#Object-oriented programming (OOP)

#Q1 Create a Car class with attributes like brand and model. Then create an instance of this class

class Car:
    totalObj = 0
    def __init__(self, brand, model):
        self.__brand = brand #encapsulation
        self.__model = model
        Car.totalObj += 1 #Q6
    
    def get_brand(self):
        return self.__brand + " !"
    
    def fuel_type(self):
        return "Petrol Or Deisel"
#Q2  Add a method to the Car class that displays the full name of the car (brand and model).
    def fullName(self):
        mycarname = f"{self.__brand} {self.__model}"
        return mycarname
    
    @staticmethod #Q7
    def general_description():
        return "Cars are means of transport"
    @property #Q8
    def model(self):
        return self.__model



my_car = Car("Tata", "Punch")
print(my_car.get_brand())
print(my_car.model)
print(my_car.fullName())

#Q3  Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Battry"

my_car01 = ElectricCar("Renault", "Duster", "98kwh")
print(my_car01.get_brand())
print(my_car01.model)
print(my_car01.battery_size)
print(my_car01.fullName())
    
#Q4 Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
       
#Q5 Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
my_car02 = Car("Tata", "Nexon")
my_car03 = ElectricCar("Tesla", "Baigan", "107kwh")
#polymorphism
print(my_car02.fuel_type()) 
print(my_car03.fuel_type())

#Q6 Add a class variable to Car that keeps track of the number of cars created.

print(Car.totalObj)

#Q7 Add a static method to the Car class that returns a general description of a car.

print(my_car.general_description())
print(Car.general_description())

#Q8 Use a property decorator in the Car class to make the model attribute read-only.

print(my_car.model)

#Q9 Use a property decorator in the Car class to make the model attribute read-only.

print(isinstance(my_car03, Car))
print(isinstance(my_car, ElectricCar))
print(isinstance(my_car03, ElectricCar))

#Q10 Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())