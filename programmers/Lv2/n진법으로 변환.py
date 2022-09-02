def solution(n, t, m, p):
    charMap = '0123456789ABCDEF'
    
    # n진법으로 변환
    def transform(num, q):
        if num == 0: return '0'
        rev = ''
        while num > 0:
            num, mod = divmod(num, q)
            rev += charMap[mod]
        return rev[::-1]
            
    word = ''
    for i in range(m * t):
        word += transform(i, n)
    
    return word[p-1::m][:t]