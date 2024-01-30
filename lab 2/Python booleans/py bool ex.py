#1 EX.
print(10 > 9)
print(10 == 9)
print(10 < 9)
#2 EX.
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#3 EX.
print(bool("Hello"))
print(bool(15))
#4 EX.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#5 EX.
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#6 EX.
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
#7 EX.
def myFunction() :
  return True

print(myFunction())
#8 EX.
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#9 EX.
  x = 200
print(isinstance(x, int))

