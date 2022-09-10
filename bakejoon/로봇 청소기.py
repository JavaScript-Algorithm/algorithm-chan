# d: 북(0), 동(1), 남(2), 서(3)

n, m = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
move = [(-1,0),(0,1),(1,0),(0,-1)]

def getDir(d):
    moveList = [(-1,0),(0,1),(1,0),(0,-1)]
    return moveList[d]
    
def solution(r, c, d, first):
    if first:
        # 현재 위치 청소
        grid[r][c] = 2 
    
    # 3. 네 방향 모두 청소가 이미 되어 있거나 벽인 경우
    check = [0] * 4
    for i in range(4):
        nr, nc = r + move[i][0], c + move[i][1]
        if grid[nr][nc] == 1 or grid[nr][nc] == 2:
            check[i] = 1
    if len(list(filter(lambda x: x == 1, check))) == 4:
        # 4. 뒤쪽 방향이 벽이라 후진할 수 없는 경우 멈춘다
        m = getDir(d)
        nr = r - m[0] 
        nc = c - m[1]
        if grid[nr][nc] == 1:
            return
        else:
            # 후진 가능하면 후진한다
            solution(nr, nc, d, False)
    else:
        nextD = d - 1 # 왼쪽 방향
        if nextD == -1:
            nextD = 3
        nm = getDir(nextD)
        nr = r + nm[0]
        nc = c + nm[1]
        
        # 1. 왼쪽 방향 값이 0이면
        if grid[nr][nc] == 0:
            # 회전 후 전진하고 1번부터 진행
            grid[nr][nc] = 2
            solution(nr, nc, nextD, True)
        else:
            # 2. 왼쪽 방향에 청소할 공간이 없으면, 회전하고 2번으로 돌아간다
            solution(r, c, nextD, False)
    
solution(r, c, d, True)

cleaned = [0 for i in range(n) for j in range(m) if grid[i][j] == 2]
print(len(cleaned))
