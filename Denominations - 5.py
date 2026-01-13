A = int(input())
result1 = A // 2000
a = (A - (2000 * result1))
result2 = a // 500
b = (A - (2000 * result1) - (500 * result2))
result3 = b // 200 
c = (A - (2000 * result1) - (500 * result2) - (200 * result3))
result4 = c // 50
d = (A - (2000 * result1) - (500 * result2) - (200 * result3) - (50 * result4))
result5 = d // 20
e = (A - (2000 * result1) - (500 * result2) - (200 * result3) - (50 * result4) - (20 * result5))
result6 = e // 5
f = (A - (2000 * result1) - (500 * result2) - (200 * result3) - (50 * result4) - (20 * result5) - (5 * result6))
result7 = f // 2
g = (A - (2000 * result1) - (500 * result2) - (200 * result3) - (50 * result4) - (20 * result5) - (5 * result6) - (2 * result7))
result8 = g // 1


print("2000:" + str(result1) + " 500:" + str(result2) + " 200:" + str(result3) + " 50:" + str(result4) + " 20:" + str(result5) + " 5:" + str(result6) + " 2:" + str(result7) + " 1:" + str(result8))