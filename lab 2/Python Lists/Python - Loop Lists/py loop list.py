#1 EX.
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#2 EX.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#3 EX.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#4 EX.
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]