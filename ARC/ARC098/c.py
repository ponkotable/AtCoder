n = int(input())
s = input()
w_sum = 0
e_sum = 0
w_list = []
e_list = []
for i in range(n):
    if s[i] == 'W':
        w_sum += 1
    else:
        e_sum += 1
    w_list.append(w_sum)
    e_list.append(e_sum)

ans = n+1
for i in range(1, n-1):
    ans = min(ans, w_list[i] + e_list[-1] - e_list[i+1])
ans = min(ans, e_list[-1] - e_list[0])
ans = min(ans, w_list[-2])
print(ans)
