#Sidenote: I will transfer these to a .ipynb file when I get home I can't do that on Replit

import random as rng

while True:
  prev_num = rng.randint(0, 100)
  next_num = rng.randint(0, 100)

  if prev_num % 2 == 0 and next_num % 2 == 0:
    print(f'Two even values have been generated, those two numbers are ({prev_num}, {next_num})')
    break      #I decided against using a flag, it doesn't seem very practical
  else:
    print(prev_num, next_num)