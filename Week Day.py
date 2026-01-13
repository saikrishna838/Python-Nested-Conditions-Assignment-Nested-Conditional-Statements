n = int(input())
if (n == 1) or (n == 2):
    print("Week Start")
elif 3 <= n <= 5:
    print("Midweek")
elif (n == 6) or (n == 7):
    print("Weekend")