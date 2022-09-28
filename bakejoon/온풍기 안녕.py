from collections import deque

# 오, 왼, 위, 아
move = [[0,1], [0, -1], [-1,0], [1,0]]

# 오른쪽 검사할 때 
# 1) 오위: (x,y,0) 또는 (x-1, y, 1) 이면 못감
# 2) 오: (x,y,1)이면 못감
# 2) 오아: (x+1, y, 0) 또는 (x+1, y, 1)이면 못감

# 왼쪽 검사할 때
# 1) 왼위: (x,y,0) 또는 (x-1, y-1, 1) 이면 못감
# 2) 왼: (x,y-1,1) 이면 못감
# 3) 왼아: (x+1,y,0) 또는 (x+1, y-1,1) 이면 못감

# 위 검사
# 1) 위왼: (x,y-1,1) 또는 (x,y-1,0) 이면 못감
# 2) 위: (x,y,0) 이면 못감
# 3) 위오: (x,y,1) 또는 (x,y+1,0) 이면 못감

# 아 검사
# 1) 아왼: (x,y-1,1) 또는 (x+1, y-1,0) 이면 못감
# 2) 아: (x+1,y,0) 이면 못감
# 3) 아오: (x,y,1) 또는 (x+1, y+1,1) 이면 못감

def isValid(r, c, n, m):
    return 0 <= r < n and 0 <= c < m

def wind(grid, wallZero, wallOne, r, c, d, n, m):
    newGrid = [[0] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    r, c = r + move[d][0], c + move[d][1]
    newGrid[r][c] = 5
    visit[r][c] = 1

    queA = deque([[r, c]])
    queB = deque()

    for i in range(4, 0, -1):
        while len(queA) > 0:
            r, c = queA.popleft()

            if d == 0: # 오른쪽
                if isValid(r-1, c, n, m):
                    if wallZero[r][c] == 0 and wallOne[r-1][c] == 0:
                        if isValid(r-1, c+1, n, m):
                            newGrid[r-1][c+1] = i
                            if visit[r-1][c+1] == 0:
                                queB.append([r-1, c+1])
                            visit[r-1][c+1] = 1
                if wallOne[r][c] == 0:
                    if isValid(r, c+1, n, m):
                        newGrid[r][c+1] = i
                        if visit[r][c+1] == 0:
                            queB.append([r, c+1])
                        visit[r][c+1] = 1
                if isValid(r+1, c, n, m):
                    if wallZero[r+1][c] == 0 and wallOne[r+1][c] == 0:
                        if isValid(r+1, c+1, n, m):
                            newGrid[r+1][c+1] = i
                            if visit[r+1][c+1] == 0:
                                queB.append([r+1, c+1])
                            visit[r+1][c+1] = 1
            if d == 1: # 왼쪽
                if isValid(r-1, c-1, n, m):
                    if wallZero[r][c] == 0 and wallOne[r-1][c-1] == 0:
                        newGrid[r-1][c-1] = i
                        if visit[r-1][c-1] == 0:
                            queB.append([r-1, c-1])
                        visit[r-1][c-1] = i
                if isValid(r, c-1, n, m):
                    if wallOne[r][c-1] == 0:
                        newGrid[r][c-1] = i
                        if visit[r][c-1] == 0:
                            queB.append([r, c-1])
                        visit[r][c-1] = 1
                if isValid(r+1, c-1, n, m):
                    if wallZero[r+1][c] == 0 and wallOne[r+1][c-1] == 0:
                        if isValid(r+1, c-1, n, m):
                            newGrid[r+1][c-1] = i
                            if visit[r+1][c-1] == 0:
                                queB.append([r+1, c-1])
                            visit[r+1][c-1] = 1
            if d == 2: # 위 
                if isValid(r, c-1, n, m):
                    if wallZero[r][c-1] == 0 and wallOne[r][c-1] == 0:
                        if isValid(r-1, c-1, n, m):
                            newGrid[r-1][c-1] = i
                            if visit[r-1][c-1] == 0:
                                queB.append([r-1, c-1])
                            visit[r-1][c-1] = 1
                if wallZero[r][c] == 0:
                    if isValid(r-1, c, n, m):
                        newGrid[r-1][c] = i
                        if visit[r-1][c] == 0:
                            queB.append([r-1, c])
                        visit[r-1][c] = 1
                if isValid(r, c+1, n, m):
                    if wallZero[r][c+1] == 0 and wallOne[r][c] == 0:
                        if isValid(r-1, c+1, n, m):
                            newGrid[r-1][c+1] = i 
                            if visit[r-1][c+1] == 0:
                                queB.append([r-1, c+1])
                            visit[r-1][c+1] = 1
            if d == 3: # 아래
                if isValid(r+1, c-1, n, m):
                    if wallZero[r+1][c-1] == 0 and wallOne[r][c-1] == 0:
                        if isValid(r+1, c-1, n, m):
                            newGrid[r+1][c-1] = i
                            if visit[r+1][c-1] == 0:
                                queB.append([r+1, c-1])
                            visit[r+1][c-1] = 1
                if isValid(r+1, c, n, m):
                    if wallZero[r+1][c] == 0:
                        newGrid[r+1][c] = i
                        if visit[r+1][c] == 0:
                            queB.append([r+1, c])
                        visit[r+1][c] = 1
                if isValid(r+1, c+1, n, m):
                    if wallZero[r+1][c+1] == 0 and wallOne[r][c] == 0:
                        newGrid[r+1][c+1] = i
                        if visit[r+1][c+1] == 0:
                            queB.append([r+1, c+1])
                        visit[r+1][c+1] = 1
        while len(queB) > 0:
            queA.append(queB.pop())
    
    # grid에 newGrid 더해준다
    for i in range(n):
        for j in range(m):
            grid[i][j] += newGrid[i][j]
            
def updateDegrees(grid, wallZero, wallOne, n, m):
    # 오: [r, c, 1]
    # 왼: [r, c-1, 1]
    # 위: [r, c, 0]
    # 아: [r+1, c, 0]
    newGrid = [block.copy() for block in grid]

    for r in range(n):
        for c in range(m):
            myDegree = newGrid[r][c]
            for d in range(4):
                dr, dc = move[d]
                nr, nc = r + dr, c + dc
                flag = False
                if isValid(nr, nc, n, m):
                    if d == 0:
                        if wallOne[r][c] == 0:
                            flag = True 
                    if d == 1:
                        if isValid(r, c-1, n, m):
                            if wallOne[r][c-1] == 0:
                                flag = True 
                    if d == 2:
                        if wallZero[r][c] == 0:
                            flag = True
                    if d == 3:
                        if isValid(r+1, c, n, m):
                            if wallZero[r+1][c] == 0:
                                flag = True 
                    if flag:
                        if myDegree > newGrid[nr][nc]:
                            offset = (myDegree - newGrid[nr][nc]) // 4
                            grid[r][c] -= offset
                            grid[nr][nc] += offset
                            

def solution():
    n, m, K = list(map(int, input().split()))
    gridInfo = [list(map(int, input().split())) for _ in range(n)]
    w = int(input())
    walls = [list(map(int, input().split())) for _ in range(w)]
    walls = list(map(lambda x: [x[0]-1, x[1]-1, x[2]], walls))
    grid = [[0] * m for _ in range(n)]
    wallZero = [[0] * m for _ in range(n)] 
    wallOne = [[0] * m for _ in range(n)]
    
    # 벽 배열 설정
    for r, c, t in walls:
        if t == 0:
            wallZero[r][c] = 1
        elif t == 1:
            wallOne[r][c] = 1

    # 온풍기 위치 및 방향, 체크할 위치
    machines = []
    checkLocs = []
    for i in range(n):
        for j in range(m):
            if gridInfo[i][j] == 5: checkLocs.append([i, j])
            elif gridInfo[i][j] > 0: machines.append([i, j, gridInfo[i][j]-1])

    ans = 0
    while True:
        # 1. 집에 있는 온풍기에서 바람이 한 번 나옴 5 -> 1. 
        for r, c, d in machines:
            wind(grid, wallZero, wallOne, r, c, d, n, m)
        
        # 2. 온도가 조절됨
        updateDegrees(grid, wallZero, wallOne, n, m)

        # 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
        for r in range(n):
            if grid[r][0] > 0:
                grid[r][0] -= 1
            if grid[r][m-1] > 0:
                grid[r][m-1] -=1 
        
        for c in range(1, m-1):
            if grid[0][c] > 0:
                grid[0][c] -= 1
            if grid[n-1][c] > 0:
                grid[n-1][c] -= 1

        # 4. 초콜릿을 하나 먹는다.
        ans += 1

        # 5. 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 만족하면 멈춘다
        flag = True
        for r, c in checkLocs:
            if grid[r][c] < K:
                flag = False
                break
        
        if flag:
            return ans

        if ans > 100:
            return 101

print(solution())
