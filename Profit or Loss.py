cp = int(input())
sp = int(input())
if cp < sp:
    print("Profit")
elif cp > sp:
    print("Loss")
elif sp == cp:
    print("No Profit - No Loss")