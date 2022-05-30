n, a, b = map(int, input().split())
mod = pow(10, 9) + 7
all = pow(2, n, mod) - 1

def comb(n, r):
    numerator = 1
    denominator = 1
    r = min(n-r, r)
    for i in range(r):
        numerator *= n - i
        numerator %= mod
        denominator *= r - i
        denominator %= mod
    return numerator * pow(denominator, mod-2, mod) % mod

nca = comb(n, a)
ncb = comb(n, b)
all -= nca + ncb
print(all%mod)
