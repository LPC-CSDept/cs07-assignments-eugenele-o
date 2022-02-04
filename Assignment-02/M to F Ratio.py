malecount = int(input('How many males are in your class?: '))
femalecount = int(input('How many females are in your class?: '))

totalstudents = malecount + femalecount

malepercent = malecount / totalstudents
femalepercent = femalecount / totalstudents

print('The total number of males in your class is', format(malepercent, '.2%'), 'and the total number of females in your class is', format(femalepercent, '.2%'))