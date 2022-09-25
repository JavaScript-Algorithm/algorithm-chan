import math

move = [[0,-1],[1,0],[0,1],[-1,0]] # 왼 아 오 위

windx = [
    # left
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    # down
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    # right
    [1, -1, 2, -2, 0, 1, -1, 1, -1],
    # up
    [1, 1, 0, 0, -2, 0, 0, -1, -1]
]
windy = [
    # left
    [1, 1, 0, 0, -2, 0, 0, -1, -1],
    # down
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    # right
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    # up
    [1, -1, 2, -2, 0, 1, -1, 1, -1]
]

rate = [0.01, 0.01, 0.02, 0.02, 0.05, 0.07, 0.07, 0.1, 0.1]

def moveSand(grid, x, y, d, n):
    outSand = sandSum = 0
    mySand = grid[x][y]
    
    for i in range(9):
        nx = x + windx[d][i]
        ny = y + windy[d][i]
        sand = math.floor(mySand * rate[i])
        sandSum += sand # 날라간 모래합

        # 모래가 격자 넘어가는 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            outSand += sand
            continue

        grid[nx][ny] += sand

    remain = mySand - sandSum 

    # 나머지
    nx = x + move[d][0]
    ny = y + move[d][1]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        outSand += remain
    else:
        grid[nx][ny] += remain

    return outSand

        
def solution():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]    
    ans = 0
    Tr = Tc = n // 2
    d = 3

    for k in range(1, n):
        for _ in range(2):
            d = (d + 1) % 4
            for _ in range(k):
                # 토네이도 이동
                Tr, Tc = Tr + move[d][0], Tc + move[d][1]
                ans += moveSand(grid, Tr, Tc, d, n)
                grid[Tr][Tc] = 0
                

    d = (d + 1) % 4
    for _ in range(n-1):
        Tr, Tc = Tr + move[d][0], Tc + move[d][1]
        ans += moveSand(grid, Tr, Tc, d, n)
        grid[Tr][Tc] = 0

    print(ans)

solution()
