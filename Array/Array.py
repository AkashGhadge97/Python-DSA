noOfDays =  int(input("Enter the number of days:"))
total=0
dayList=[]
for i in range(1,noOfDays+1):
    nextDay = int(input("Day" + str(i) + "'s high temperature:"))
    dayList.append(nextDay)
    total+=nextDay
avg = round(total/noOfDays,2)
print("\nAverage Temperature:",avg)
count=0
for i in dayList:
    if i > avg:
        count+=1
print(str(count) + " days above average temperature")