from itertools import product

def getPopulation(grid, visit, x, y, d1, d2, n):
    populations = [0] * 5

    # 5번 선거구 표시
    for i in range(0, d1+1):
        visit[x+i][y-i] = 5
        visit[x+d2+i][y+d2-i] = 5
    for i in range(0, d2+1):
        visit[x+i][y+i] = 5
        visit[x+d1+i][y-d1+i] = 5
    
    #up = [x, y]
    #down = [x+d1+d2, y-d1+d2]
    #left = [x+d1, y-d1]
    #right = [x+d2, y+d2]

    for r in range(1, x): visit[r][y] = 1
    for c in range(1, y-d1): visit[x+d1][c] = 3
    for c in range(y+d2+1, n+1): visit[x+d2][c] = 2
    for r in range(x+d1+d2+1, n+1): visit[r][y-d1+d2] = 4

    # 1구역
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if visit[i][j] == 1 or visit[i][j] == 5: break
            visit[i][j] = 1
    
    # 2구역
    for i in range(1, x+d2+1):
        for j in range(n, y, -1):
            if visit[i][j] == 2 or visit[i][j] == 5: break
            visit[i][j] = 2
    
    # 3구역
    for i in range(x+d1, n+1):
        for j in range(1, y-d1+d2):
            if visit[i][j] == 3 or visit[i][j] == 5: break
            visit[i][j] = 3

    # 4구역
    for i in range(x+d2+1, n+1):
        for j in range(n, y-d1+d2-1, -1):
            if visit[i][j] == 4 or visit[i][j] == 5: break
            visit[i][j] = 4
    
    # 인구수 구하기 및 visit 초기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            if visit[i][j] == 1: populations[0] += grid[i][j]
            elif visit[i][j] == 2: populations[1] += grid[i][j]
            elif visit[i][j] == 3: populations[2] += grid[i][j]
            elif visit[i][j] == 4: populations[3] += grid[i][j]
            else: populations[4] += grid[i][j]
            visit[i][j] = 0

    # 최대, 최소값 차이 반환
    return max(populations) - min(populations)


def solution():
    n = int(input())
    grid = [[0] * (n+1)]
    for _ in range(n):
        grid.append([0] + list(map(int, input().split())))
    
    visit = [[0] * (n+1) for _ in range(n+1)]
    candidates = [[x for x in range(1, n+1)], [x for x in range(1, n+1)]]
    
    ans = 1e9
    for x in range(1, n+1):
        for y in range(1, n+1):
            for d1, d2 in product(*candidates):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y-d1 < y < y+d2 <= n:
                    ans = min(ans, getPopulation(grid, visit, x, y, d1, d2, n))
    print(ans)

solution()