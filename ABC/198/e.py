n = int(input())
c = map(int, input().split())
for i in range(n):
    a, b = map(int, input().split())
    c[a-1].append(b)
    c[b-1].append(a)

queue = []
for node in c[0][1:]:
    queue.append(node)

while len(queue) != 0:
    node = queue[0]
    
    if len(queue) == 1:
        queue = []
    else:
        queue = queue[1:]
