import random as rng
student_names = ['Bill', 'Jack', 'Joe', 'Tim', 'Zoe']
totalrows = int(input("Enter the # of Students: "))
totalcolumns = int(input("Enter the # of Scores: "))

list1 = []
for i in range(totalrows):
  row = []
  for j in range(totalcolumns):
    row.append(rng.randint(50, 100))
  list1.append(row)

for i in range(totalrows):
  for j in range(totalcolumns):
    print(list1[i][j], end = " ")
  print()
  
for i in range(totalrows):
  sum1 = sum(list1[i])  
  print(sum1)

for i in range(totalcolumns):
  sum2 = 0
  for j in range(totalrows):
    sum2 += list1[j][i]
    print(sum2)