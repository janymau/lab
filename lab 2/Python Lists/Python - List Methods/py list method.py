#1 EX.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#2 EX.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#3 EX.
newlist = [x for x in fruits if x != "apple"]
#4 EX.
newlist = [x for x in fruits]
#5 EX.
newlist = [x for x in range(10)]
#6 EX.
newlist = [x for x in range(10) if x < 5]
#7 EX.
newlist = [x.upper() for x in fruits]
#8 EX.
newlist = ['hello' for x in fruits]
#9 EX.
newlist = [x if x != "banana" else "orange" for x in fruits]
