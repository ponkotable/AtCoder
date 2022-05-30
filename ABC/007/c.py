r, c = map(int, input().split())
sy , sx = map(int, input().split())
gy, gx = map(int, input().split())
table = []
for i in range(r):
    table.append(list(input()))
queue = [(sy-1, sx-1, 0)]
while len(queue) != 0:
    y, x, ans = queue.pop(0)
    if y == gy-1 and x == gx-1:
        print(ans)
        exit()
    for ny, nx in [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]:
        if table[ny][nx] == '.':
            queue.append((ny, nx, ans+1))
            table[ny][nx] = '#'
