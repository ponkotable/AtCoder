n = int(input())
memo = list(map(int, input().split()))
for i in range(1, n):
    # print(memo)
    tmp = list(map(int, input().split()))
    memo2 = memo.copy()
    memo[0] = tmp[0] + max(memo2[1], memo2[2])
    memo[1] = tmp[1] + max(memo2[0], memo2[2])
    memo[2] = tmp[2] + max(memo2[0], memo2[1])
print(max(memo))
