def prime(N):
    i=2
    ans = []
    n=N
    while i*i <=N:
    	while n%i==0:
    		n=n//i
    		ans.append(i)
    	i+=1
    if n != 1:
        ans.append(n)
    return ans


n, m = map(int, input().split())
a = map(int, input().split())
p_list = set()
for i in a:
    p_list = p_list | set(prime(i))
# print(list(p_list))


table = set(range(1, m+1))
for i in p_list:
    mul = 1
    while i * mul <= m:
        table.discard(i*mul)
        mul += 1

print(len(table))
for i in table:
    print(i)
