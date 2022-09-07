from math import factorial

def solution(n, k):
    arr = [i for i in range(1, n+1)]
    ans = []
    
    while n > 0:
        denom = factorial(n-1)
        index = (k-1) // denom
        k = k % denom
        ans.append(arr.pop(index))
        n -= 1
    return ans      