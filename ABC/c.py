n, m = map(int, input().split())
step = [0] * (n+2)
broken = set()
for i in range(m):
    broken.add(int(input()))
step[0] = 1
for i in range(n):
    if not i+1 in broken:
        step[i+1] += step[i]
    if not i+2 in broken:
        step[i+2] += step[i]
print(step[n] % 1000000007)
