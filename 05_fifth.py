#Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])

print(len(thisdict))

print('--------------')

# Duplicate values will overwrite existing values:

thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict1)

x = thisdict1.get("model")
print(x)

print('--------------')

y = thisdict.keys()
z = thisdict.values()
print(y)
print(z)

for a in y :
    print(thisdict[a])

print('--------------')

# Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x1 = car.keys()

print(x1) #before the change

car["color"] = "white"

print(x1) #after the change

print('--------------')

thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2["year"] = 2018
print(thisdict2)

thisdict2.update({"year": 2024})
print(thisdict2)

print('--------------')

thisdict2["color"] = "red"
print(thisdict2)

# Add a color item to the dictionary by using the update() method:

thisdict2.update({"color2nd": "black"})
print(thisdict2)

print('--------------')

# Remove Dictionary Items

user = {
    "name": "Banrakash",
    "age": 43,
    "mob": 1234567890
}

print(user)
user.pop("name")
print(user)

user.popitem()
print(user)

print('--------------')

#  Copy Dictionaries

thisdict3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict3.copy()
print(mydict)
print('--------------')

#another method for copy
mydict1 = dict(thisdict3)
print(mydict1)

print('--------------')

# Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)