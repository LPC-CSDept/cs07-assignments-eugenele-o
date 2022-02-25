#Sidenote: I will transfer these to a .ipynb file when I get home I can't do that on Replit

keyword = 'stop'
sum = 0

while True:
  user_input = input('Please input anything: ').lower()
  if 'p' in user_input:
    sum += 1
  if user_input == keyword:
    break
print(f'There were {sum} p\'s in the strings you input!')