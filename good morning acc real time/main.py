import time
timestamp=time.strftime('%H Hours\n%M minutes\n%S seconds\n')
print(timestamp)
Hour=int(time.strftime('%H '))
print(Hour)
if Hour>0 and Hour<12:
    print("Good morning sir")
elif (Hour>12 and Hour<17):
    print("Good Afternoon sir")
elif (Hour>17 and Hour<19):
    print("Good evening sir")
else:
    print("Good night sir")
  
