n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = []
for i in range(n):
    d.append(b[c[i]-1])
exist = [0]*1000000
for i in range(n):
    exist[d[i]] += 1
ans = 0
for i in range(n):
    ans += exist[a[i]]
print(ans)
