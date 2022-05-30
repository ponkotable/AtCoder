l = ["ABC", "ARC", "AGC", "AHC"]
s = []
for i in range(3):
  s.append(input())
for c in l:
    if not c in s:
        print(c)
        exit()
