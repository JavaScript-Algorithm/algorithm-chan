from itertools import product

def paint(grid, i, j, paintList):
    # paintList가 0이 아닌 방향을 6이 나올때까지 감시
    # [북, 동, 남, 서]
    move = [[-1,0], [0,1], [1,0], [0,-1]]
    n, m = len(grid), len(grid[0])
    for idx in range(4):
        if paintList[idx] != 0:
            r, c = i + move[idx][0], j + move[idx][1]

            while r >= 0 and r < n and c >= 0 and c < m:
                if grid[r][c] == 6: break
                grid[r][c] = -1
                r, c = r + move[idx][0], c + move[idx][1]

def getDirAry(x):
    i, j, cctvType = x
    if cctvType == 1:
        return [[i, j, [1,0,0,0]], [i,j,[0,1,0,0]], [i,j,[0,0,1,0]], [i,j,[0,0,0,1]]]
    if cctvType == 2:
        return [[i, j, [1,0,1,0]], [i,j,[0,1,0,1]]]
    if cctvType == 3:
        return [[i, j, [1,1,0,0]], [i,j,[0,1,1,0]], [i,j,[0,0,1,1]], [i,j,[1,0,0,1]]]
    if cctvType == 4:
        return [[i, j, [1,1,1,0]], [i,j,[0,1,1,1]], [i,j,[1,0,1,1]], [i,j,[1,1,0,1]]]
    if cctvType == 5:
        return [[i, j, [1,1,1,1]]]

def solution():
    n, m = list(map(int, input().split()))
    gridOrigin = [list(map(int, input().split())) for _ in range(n)]

    # cctv 위치 추출
    cctvLocs = [[i, j, gridOrigin[i][j]] for i in range(n) for j in range(m) if gridOrigin[i][j] not in [0, 6]]
    cctvLocs = list(map(getDirAry, cctvLocs))
    ans = 1e9

    # cctv
    for cctvLoc in product(*cctvLocs):
        grid = [block.copy() for block in gridOrigin]
        for i, j, detectList in cctvLoc:
            paint(grid, i, j, detectList)
    
            cnt = len([0 for r in range(n) for c in range(m) if grid[r][c] == 0])
            ans = min(ans, cnt)
    cnt = len([0 for i in range(n) for j in range(m) if gridOrigin[i][j] == 0])
    ans = min(ans, cnt)
    print(ans)

solution()