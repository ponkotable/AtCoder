n = int(input())
a = list(map(int, input().split()))
ans = 0
for k in range(1, n+1):
    s = sum(a[:k])
    ans = s
    for i in range(n-k):
        s -= a[i]
        s += a[i+k]
        ans = max(ans, s)
    print(ans)
