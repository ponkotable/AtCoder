n, q = map(int, input().split())
s = input()
ans = [0]
sum = 0
for i in range(1, n):
    if s[i-1] == 'A' and s[i] == 'C':
        sum += 1
    ans.append(sum)
for i in range(q):
    l, r = map(int, input().split())
    print(ans[r-1] - ans[l-1])    
