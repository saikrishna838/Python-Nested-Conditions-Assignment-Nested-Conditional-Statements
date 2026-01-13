d = input()
n = int(input())

if d == "Sunday":
    day = 0
elif d == "Monday":
    day = 1
elif d == "Tuesday":
    day = 2
elif d == "Wednesday":
    day = 3
elif d == "Thursday":
    day = 4
elif d == "Friday":
    day = 5
elif d == "Saturday":
    day = 6

target_day = day + n - 1

if(target_day % 7 == 0):
    print("Sunday")
elif(target_day % 7 == 1):
    print("Monday")
elif(target_day % 7 == 2):
    print("Tuesday")
elif(target_day % 7 == 3):
    print("Wednesday")
elif(target_day % 7 == 4):
    print("Thursday")
elif(target_day % 7 == 5):
    print("Friday")
elif(target_day % 7 == 6):
    print("Saturday")
    