s = input()
t = input()
i = 0
flag = False
while i <= len(s)-1:
    if s[i] != t[i]:
        if flag:
            print("No")
            exit()
        if s[i+1] == t[i] and s[i] == t[i+1]:
            flag = True
            i += 1

            if i == len(s)-1:
                print("Yes")
                exit()
        else:
            print("No")
            exit()
    i += 1

if s[-1] != t[-1]:
    print("No")
else:
    print("Yes")
