user_int = 5 
user_ints = []
sum = 0

for i in range(user_int):
  user_int = int(input('Enter any number: '))
  sum += user_int
  user_ints.insert(i, user_int)
print(f'The total numbers input were {user_ints}')

sum2 = sum
sum2 -= min(user_ints)
sum2 -= max(user_ints)
user_ints.remove(min(user_ints))
user_ints.remove(max(user_ints))
print(f'The total sum of all numbers is {sum}')

average = sum2 / len(user_ints)
print('The mathematical average number is {:.2f} as a decimal'.format(average))