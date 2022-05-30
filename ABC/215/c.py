import itertools
s, k = input().split()
all_str = []
for str in set(itertools.permutations(s)):
    all_str.append(''.join(str))
all_str = sorted(all_str)
print(all_str[int(k)-1])
