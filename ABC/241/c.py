def count(table, n, i, j, pi, pj):
    black, white = 0, 0
    for c in range(6):
        if table[i][j] == '#':
            black += 1
        else:
            white += 1
        i += pi
        j += pj
    if black >= 4:
        return True
    else:
        return False

def search(table, n, i, j):
    for pi, pj in [(-1, 1), (0, 1), (1, 1), (1, 0)]:
        if (0 <= i + 5 * pi < n) and (j + 5 * pj < n):
            if count(table, n, i, j, pi, pj):
                return True
    return False


n = int(input())
table = []
for i in range(n):
    table.append(input())

for i in range(n):
    for j in range(n):
        if search(table, n, i, j):
            print("Yes")
            exit()
print("No")
