# EX 1. Get the value of the "model" key using indexing
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# EX 2. Get the value of the "model" key using the get() method
x = thisdict.get("model")

# EX 3. Get a list of the keys
x = thisdict.keys()

# EX 4. Add a new item to the dictionary and see the keys list get updated
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)  # before the change
car["color"] = "white"
print(x)  # after the change

# EX 5. Get a list of the values
x = thisdict.values()

# EX 6. Make a change in the original dictionary, and see the values list get updated
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change

# EX 7. Add a new item to the original dictionary and see the values list get updated
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)  # before the change
car["color"] = "red"
print(x)  # after the change

# EX 8. Get a list of the key:value pairs
x = thisdict.items()

# EX 9. Make a change in the original dictionary, and see the items list get updated
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change

# EX 10. Add a new item to the original dictionary and see the items list get updated
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)  # before the change
car["color"] = "red"
print(x)  # after the change

# EX 11. Check if "model" is present in the dictionary
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
