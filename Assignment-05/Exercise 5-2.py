import random

total_gen = 10
gen_list = []

for i in range(total_gen):
  gen_int = random.randint(0,100)
  gen_list.insert(i, gen_int)
min = min(gen_list)
min_idx = gen_list.index(min)

print(f'The smallest generated number was {min}, it\'s index number is {min_idx} (From 0-9), and the list as a whole is {gen_list}')