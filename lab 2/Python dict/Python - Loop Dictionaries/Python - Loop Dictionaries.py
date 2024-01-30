# EX 1. Print all key names in the dictionary, one by one
for x in thisdict:
  print(x)

# EX 2. Print all values in the dictionary, one by one
for x in thisdict:
  print(thisdict[x])

# EX 3. Use the values() method to return values of a dictionary
for x in thisdict.values():
  print(x)

# EX 4. Use the keys() method to return the keys of a dictionary
for x in thisdict.keys():
  print(x)

# EX 5. Loop through both keys and values, by using the items() method
for x, y in thisdict.items():
  print(x, y)
