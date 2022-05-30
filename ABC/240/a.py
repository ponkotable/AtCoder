a, b = map(int, input().split())
if (a, b) == (1, 10) or (a, b) == (10, 1):
    print("Yes")
elif abs(a-b) == 1:
    print("Yes")
else:
    print("No")
