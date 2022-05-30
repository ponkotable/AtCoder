s = input()
index = -1
while s[index] == '0':
    index -= 1
if index != -1:
    s = s[:index+1]
print(s)
if s == s[::-1]:
    print("Yes")
else:
    print("No")
