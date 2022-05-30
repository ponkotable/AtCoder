s = input()
use = []
unknown = []
dont = []
for i in range(len(s)):
    if s[i] == 'o':
        use.append(str(i))
    elif s[i] == '?':
        unknown.append(str(i))
    else:
        dont.append(str(i))
ans = 0
for i in range(10000):
    num = str(i).zfill(4)
    flag = True
    for c in use:
        if not c in num:
            flag = False
    for c in dont:
        if c in num:
            flag = False

    if flag:
        ans += 1

print(ans)
