# EX 1. Create and print a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# EX 2. Print the "brand" value of the dictionary
print(thisdict["brand"])

# EX 3. Duplicate values will overwrite existing values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# EX 4. Print the number of items in the dictionary
print(len(thisdict))

# EX 5. Dictionary items can have different data types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# EX 6. Print the data type of a dictionary
print(type(thisdict))

# EX 7. Use the dict() constructor to make a dictionary
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

