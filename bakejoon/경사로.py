def isPossibleBock(block, L):
    # (높이, 연속된 수) 배열을 만든다
    info = []
    count = 0
    i = 0
    height = block[0]
    while i < len(block):
        if block[i] == height:
            count += 1
        else:
            info.append((height, count))
            height = block[i]
            count = 1
        i += 1
    info.append((height, count))
    
    # 높이가 같으면 True 
    if len(info) == 1:
        return True

    for i in range(len(info)-1):
        # 인접 높이차가 1이 아닌게 있으면 False
        if abs(info[i][0] - info[i+1][0]) > 1:
            return False
    
        # 인접한 튜플을 비교해서 높이가 낮은 쪽의 연속된 수가 L 미만이면 fail
        if info[i][0] < info[i+1][0]:
            if info[i][1] < L: 
                return False
        elif info[i][0] > info[i+1][0]:
            if info[i+1][1] < L:
                return False

    # 212처럼 계곡 모양이고 중간에 연속된 수가 L*2 미만이면 fail
    for i in range(1, len(info)-1):
        if info[i-1][0] -1 == info[i][0] and info[i+1][0] - 1 == info[i][0]:
            if info[i][1] < L*2:
                return False

    return True 


def solution():
    n, L = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    # 행 검사
    for block in grid:
        if isPossibleBock(block, L):
            ans += 1
    
    # 열 검사
    for c in range(n):
        block = [grid[r][c] for r in range(n)]
        if isPossibleBock(block, L):
            ans += 1
        
    print(ans)

solution()