n = int(input())
a = list(map(int, input().split()))
sum = [0]
for i in range(n):
    sum.append(sum[-1] + a[i])
# print(sum)
dict = {}
ans = 0
for i in sum:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for key in dict:
    if dict[key] != 1:
        ans += dict[key]*(dict[key]-1)/2

print(int(ans))
