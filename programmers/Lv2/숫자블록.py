def getNum(n):
    if n == 1: return 0
    
    divide = 2
    while divide <= (n ** 0.5):
        if n % divide == 0:
            if n // divide > 10000000:
                divide += 1
                continue
            return n // divide
        divide += 1
    return 1
    
def solution(begin, end):
    ans = []
    
    for i in range(begin, end + 1):
        ans.append(getNum(i))
    return ans