from collections import deque
# 모든 점에 대해 동서남북 검사
# L <= 차이 <= R 이면 국경 오픈 (set에 저장)

def getUnion(grid, visit, L, R, r, c, n):
    move = [[1,0], [0,1], [-1,0], [0,-1]]
    
    union = deque([[r, c]])
    que = deque([[r, c]])
    visit[r][c] = 1
    
    while len(que) > 0:
        r, c = que.popleft()
        
        for i in range(4):
            nr = r + move[i][0]
            nc = c + move[i][1]

            if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
            if visit[nr][nc]: continue
            if L <= abs(grid[r][c] - grid[nr][nc]) <= R:
                que.append([nr, nc])
                union.append([nr, nc])
                visit[nr][nc] = 1
    
    # union이 연합
    newNum = sum(list(map(lambda x: grid[x[0]][x[1]], list(union)))) // len(union)
    for r, c in union:
        grid[r][c] = newNum

    return len(union) > 1 


def solution():
    n, L, R = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0] * n for _ in range(n)]
    day = -1

    while True:
        flag = True 
        day += 1
        for i in range(n):
            for j in range(n):
                visit[i][j] = 0

        for i in range(n):
            for j in range(n):
                if visit[i][j] == 0:
                    if getUnion(grid, visit, L, R, i, j, n):
                        flag = False
        if flag:
            break

    print(day)

solution()