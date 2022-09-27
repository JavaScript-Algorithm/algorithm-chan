move = [[-1,0],[1,0],[0,-1],[0,1]]
dx = [0,1,0,-1]
dy = [-1,0,1,0]

def getElems(grid):
    n = len(grid)
    newElems = []
    x = y = n // 2
    cnt, d = 1, 0
    for _ in range(n-1):
        for _ in range(2):
            for _ in range(cnt):
                x = x + dx[d]
                y = y + dy[d]
                if grid[x][y] != 0:
                    newElems.append(grid[x][y])
            d = (d + 1) % 4
        cnt += 1

    for _ in range(cnt-1):
        x = x + dx[d]
        y = y + dy[d]
        if grid[x][y] != 0:
            newElems.append(grid[x][y])
    return newElems

def getElemInfo(elems):
    # [개수, 번호]로 정리
    info = []
    num = -1
    cnt = 0
    for i in range(len(elems)):
        if num == elems[i]:
            cnt += 1
        else:
            if num != -1:
                info.append([cnt, num])
            num = elems[i]
            cnt = 1
    if num != -1:
        info.append([cnt, num])
    return info

# 토네이도 생성 함수
def generateGrid(n, newElems):
    x = y = n // 2
    cnt, d = 1, 0
    newGrid = [[0] * n for _ in range(n)]
    idx = 0
    for _ in range(n-1):
        for _ in range(2):
            for _ in range(cnt):
                x = x + dx[d]
                y = y + dy[d]
                newGrid[x][y] = newElems[idx]
                idx += 1
                if idx >= len(newElems):
                    return newGrid
            d = (d + 1) % 4
        cnt += 1

    for _ in range(cnt-1):
        x = x + dx[d]
        y = y + dy[d]
        newGrid[x][y] = newElems[idx]
        idx += 1
        if idx >= len(newElems):
            return newGrid
    return newGrid

def solution():
    N, M = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(N)]
    info = [list(map(int, input().split())) for _ in range(M)]
    info = list(map(lambda x: [x[0]-1, x[1]], info))
    removedInfo = [0,0,0]

    for d, s in info:
        # 1. 블리자드 시전(얼음 파괴)
        x = y = N // 2
        for _ in range(s):
            x, y = x + move[d][0], y + move[d][1]
            grid[x][y] = 0

        # 2. 이동
        newElems = getElems(grid)
        
        # 3. 연속된 번호 4개 있으면 파괴, 이동을 반복
        while True:
            prevLen = len(newElems)
            elemInfo = getElemInfo(newElems)
            for cnt, num in elemInfo:
                if cnt >= 4:
                    removedInfo[num-1] += cnt
            newElems = [num for cnt, num in elemInfo for _ in range(cnt) if cnt < 4]
            if len(newElems) == prevLen:
                break
        
        # newElems이 비어있는 경우
        if len(newElems) == 0:
            break 

        # 4. 구슬 변화. [cnt, num]
        elemInfo = getElemInfo(newElems)
        newElems = []
        for elem in elemInfo:
            newElems += elem
        newElems = newElems[:N*N]
      
        # 새로운 grid 생성
        grid = generateGrid(N, newElems)
    
    for i in range(3):
        removedInfo[i] *= (i+1)
    
    print(sum(removedInfo))

solution()