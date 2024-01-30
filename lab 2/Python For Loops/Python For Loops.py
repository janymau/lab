#1 EX.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#2 EX.
  for x in "banana":
   print(x)
#3 EX.
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#4 EX.
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#5 EX.
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#6 EX.
  for x in range(6):
   print(x)
#7 EX.
  for x in range(2, 6):
   print(x)
#8 EX.
  for x in range(2, 30, 3):
   print(x)
#9 EX.
  for x in range(6):
   print(x)
else:
   print("Finally finished!")
#10 EX.
for x in range(6):
  if x == 3: 
    break
  print(x)
else:
  print("Finally finished!")
#11 EX.
adj = ["red", "big", "tasty"] 
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#12 EX.
for x in [0, 1, 2]:
  pass   