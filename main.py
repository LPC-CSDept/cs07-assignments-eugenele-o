import random as rng
list1 = []

for i in range(10):
  rngVal = rng.randint(0,100)
  list1.insert(i, rngVal)
print(f'Your current list is {list1}')

tinyval = min(list1)
list1[tinyval], list1[0] = list1[0], list1[tinyval]
print(f'Your new list is {list1}')

tinyval2 = min(list1[1:])
list1[tinyval2], list1[1] = list1[1], list1[tinyval2]
print(f'The final result is {list1}')