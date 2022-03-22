import random as rng
list1 = []

for i in range(10):
  rngVal = rng.randint(0,100)
  list1.insert(i, rngVal)
print(f'Your current list is {list1}')

