import math

def perm(n, r):
    return math.factorial(n) // math.factorial(n - r)

def comb(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n, r = 9, 3
print(perm(n, r))
print(comb(n, r))