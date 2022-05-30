n = int(input())
mod = 998244353
num = [1] * 10
num[0] = 0
for i in range(n-1):
    tmp = [0] * 10
    for j in range(10):
        if j == 1:
            tmp[1] += num[j]
            tmp[2] += num[j]
        elif j == 9:
            tmp[8] += num[j]
            tmp[9] += num[j]
        else:
            tmp[j-1] += num[j]
            tmp[j] += num[j]
            tmp[j+1] += num[j]
    for j in range(10):
        num[j] = tmp[j]
        num[j] %= mod

ans = 0
for i in range(10):
    ans += num[i]
    ans %= mod
print(ans)
