def gcd(a, b):
    if b == 0:
        return a
    n, mod = divmod(a, b)
    return gcd(b, mod)

def lcm(a, b):
    return a * b / gcd(a, b)

def solution(arr):
    arr.sort()
    tmp = 1
    for n in arr:
        tmp = lcm(tmp, n)
    
    return int(tmp)