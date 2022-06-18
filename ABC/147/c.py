n = int(input())
table = [[] for _ in range(n)]
for i in range(n):
    num = int(input())
    for j in range(num):
        table[i].append(list(map(int, input().split())))

ans = 0
for mask in range(1 << n):
    sum = 0
    wrong = False
    for i in range(n):
        if (mask >> i) & 1 == 1:
            cond = table[i]
            for x, y in cond:
                if (mask >> (x-1)) & 1 == y:
                    pass
                else:
                    wrong = True
                    break
            if not wrong:
                sum += 1
        if wrong:
            sum = 0
            break
    ans = max(ans, sum)
print(ans)
