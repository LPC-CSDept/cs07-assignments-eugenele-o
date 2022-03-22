import random as rng
list1 = []

for i in range(10):
  rngVal = rng.randint(0,100)
  list1.insert(i, rngVal)
print(f'Your current list is {list1}')

tinyval = min(list1)
list1.insert(0, tinyval)
print(list1)

list1.pop(tinyval)
tinyval2 = min(list1)
print(tinyval2)