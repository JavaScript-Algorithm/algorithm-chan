def isPrime(n):
    n = int(n)
    if n == 1: return False
    if n == 2 or n == 3: return True
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def transform(n, k):
    rev = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev += str(mod)
    return rev[::-1]

def solution(n, k):
    if k != 10:
        n = transform(n, k)

    n = [x for x in str(n).split('0') if x != '']
    
    n = list(filter(isPrime, n))
    return len(n)