D = int(input())
if 0 <= D <= 50:
    result1 = (D * 3) + 100
    print(result1)
elif 51 <= D <= 100:
    a =(D - 50)
    result2 = (a * 5) + 150 + 100
    print(result2)
elif 101 <= D <= 200:
    a = (D - 50 - 50)
    result3 = (a * 6) + 150 + 250 + 100
    print(result3)
elif D > 200:
    a = (D - 50 - 50 - 100)
    result4 = (a* 10) + 150 + 250 + 600 + 100
    print(result4)