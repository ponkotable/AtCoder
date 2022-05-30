import bisect
l, q = map(int, input().split())
wood = [0, l]
for i in range(q):
    c, x = map(int, input().split())
    if c == 1:
        bisect.insort(wood, x)
    else:
        index = bisect.bisect(wood, x)
        print(wood[index] - wood[index-1])
