def solution(n):
    # 작으면 right 움직이고, 크면 left 움직인다
    ssum = left = right = 1
    ans = 0
    while right <= n:
        if ssum == n:
            ans += 1
        if ssum <= n:
            right += 1
            ssum += right            
        elif ssum > n:
            ssum -= left
            left += 1
    return ans