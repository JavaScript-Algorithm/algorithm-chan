from collections import deque

def combination(items, idx, k, lst, result):
    if len(items) == k:
        result.append(items)
        return
    for i in range(idx, len(lst)):
        combination(items + [lst[i]], i + 1, k, lst, result)

def getSafeZone(newGrid, n, m):
    # 1. 2 좌표들 전부 추출
    virus = deque([(i, j) for i in range(n) for j in range(m) if newGrid[i][j] == 2])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 2. 바이러스 전파
    while len(virus) > 0:
        x, y = virus.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if newGrid[nx][ny] == 0:
                newGrid[nx][ny] = 2
                virus.append((nx, ny))
    
    # 3. 안전지대 구하기 
    safeZone = [0 for i in range(n) for j in range(m) if newGrid[i][j] == 0]
    return len(safeZone)

def solution():
    n, m = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    
    # 0 좌표들 모음
    zero_coords = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 0]
    
    result = []
    combination([], 0, 3, zero_coords, result)
    for coords in result:
        newGrid = [x.copy() for x in grid]
        
        # coords 좌표 벽 세움
        for r, c in coords:
            newGrid[r][c] = 1
        
        # newGrid 안전지대 구하기
        ans = max(ans, getSafeZone(newGrid, n, m))
        
    return ans
    
print(solution())