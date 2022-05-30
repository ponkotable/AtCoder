n = int(input())
a = list(map(int, input().split()))
stack = []
num = 0
for i in range(n):
    if len(stack) == 0:
        stack.append([a[i], 1])
    elif stack[-1][0] != a[i]:
        stack.append([a[i], 1])
    else:
        stack[-1][1] += 1
        if stack[-1][0] == stack[-1][1]:
            num -= stack[-1][0]
            stack = stack[:-1]
    num += 1
    print(num)
