n, x = map(int, input().split())
place = set()
place.add(0)
for i in range(n):
    place_tmp = set()
    a, b = map(int, input().split())
    for j in place:
        place_tmp.add(j+a)
        place_tmp.add(j+b)
    place = place_tmp.copy()
if x in place:
    print("Yes")
else:
    print("No")
