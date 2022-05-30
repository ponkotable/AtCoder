n = int(input())
a = list(map(int, input().split()))
ans = n*(n-1)*(n-2) / (3*2)
# print(ans)
s = [0] * 2 * pow(10, 5)
for i in a:
    s[i] += 1
for i in s:
    if i >= 3:
        ans -= i*(i-1)*(i-2) / (3*2)
        ans -= (i*(i-1) / 2) * (n-2)
    elif i >= 2:
        ans -= n - 2
print(ans)
