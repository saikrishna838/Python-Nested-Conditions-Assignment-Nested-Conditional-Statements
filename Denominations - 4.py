A = int(input())
result1 = A // 100
b = (A - (100 * result1))
result2 = b // 50
c = (A -(100 * result1) - (50 * result2))
result3 = c // 20
d = (A -(100 * result1) - (50 * result2) - (20 * result3))
result4 = d // 10
print("100 Notes: " + str(result1))
print("50 Notes: " + str(result2))
print("20 Notes: " + str(result3))
print("10 Notes: " + str(result4))