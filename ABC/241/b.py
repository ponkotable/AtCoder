n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in b:
    if not i in a:
        print("No")
        exit()
    else:
        a.remove(i)
print("Yes")
