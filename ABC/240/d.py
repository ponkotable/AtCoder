import collections
n = int(input())
a = list(map(int, input().split()))
collect = collections.Counter(a)
lst = set()
for key in collect:
    if key <= collect[key]:
        lst.add(key)

index = 0
while index < n:
    if a[index] in lst:
        flag = True
        for i in range(a[index]):
            if index - i == -1:
                flag = False
                break
            if a[index-i] != a[index]:
                flag = False
                break
        if flag:
            tmp = a[index]
            a = a[:index-i] + a[index+1:]
            index -= tmp
            n -= tmp
    index += 1
    print(index)
