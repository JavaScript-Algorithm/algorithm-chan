def moveBlock(grid, t, x, y):
    r = c = 4
    if t == 1:
        # 한쪽은 고정. 나머지가 9 감소하면서 0이면 대입
        while r < 10:
            if grid[r][y] == 1: break
            r += 1
        if r == 10: grid[9][y] = 1
        else: grid[r-1][y] = 1

        while c < 10:
            if grid[x][c] == 1: break
            c += 1
        if c == 10: grid[x][9] = 1
        else: grid[x][c-1] = 1
                
    if t == 2:
        while r < 10:
            if grid[r][y] == 1 or grid[r][y+1] == 1: break
            r += 1
        if r == 10: grid[9][y] = grid[9][y+1] = 1
        else: grid[r-1][y] = grid[r-1][y+1] = 1
        
        while c < 9:
            if grid[x][c] == 1 or grid[x][c+1] == 1: break
            c += 1
        if c == 9: grid[x][8] = grid[x][9] = 1
        else: grid[x][c-1] = grid[x][c] = 1

    if t == 3:
        while r < 9:
            if grid[r][y] == 1 or grid[r+1][y] == 1: break
            r += 1
        if r == 9: grid[8][y] = grid[9][y] = 1
        else: grid[r-1][y] = grid[r][y] = 1

        while c < 10:
            if grid[x][c] == 1 or grid[x+1][c] == 1: break
            c += 1
        if c == 10: grid[x][9] = grid[x+1][9] = 1
        else: grid[x][c-1] = grid[x+1][c-1] = 1

def removeGreen(grid):
    for r in range(9, 3, -1):
        canRemove = True
        for c in range(4):
            if grid[r][c] == 0:
                canRemove = False
                break
        if canRemove:
            return [True, r]
    return [False, 0]

def removeBlue(grid):
    for c in range(9, 3, -1):
        canRemove = True
        for r in range(4):
            if grid[r][c] == 0:
                canRemove = False
                break
        if canRemove:
            return [True, c]
    return [False, 0] 

def solution():
    n = int(input())

    # t = 1: 1x1인 블록을 (x, y)에 놓은 경우
    # t = 2: 1x2인 블록을 (x, y), (x, y+1)에 놓는 경우
    # t = 3: 2x1인 블록을 (x, y), (x+1, y)에 놓는 경우
    # t, x, y
    blockInfo = [list(map(int, input().split())) for _ in range(n)]
    
    # 한 행이나 열이 타일로 가득 차서 사라지면 1점을 획득
    # 점수 획득하고 아래 또는 오른쪽으로 이동
    # 특수 칸에 블록이 존재하면 또 그만큼 이동
    score = { 'green':0, 'blue':0 }

    # 4~5행: 초 특수
    # 6~9행: 초
    # 4~5열: 파 특수
    # 6~9열: 파
    grid = [[0]*10 for _ in range(10)]
    
    for t, x, y in blockInfo:
        # 1. 블록 이동
        moveBlock(grid, t, x, y)
      
        # 2. 점수 획득 - 획득시 점수 추가, 없어진
        # 초록색 검사
        while True:            
            # 체크 - 제거할 수 있는게 없으면 break
            canRemove, removeRow = removeGreen(grid)
            if canRemove == False: break
            score['green'] += 1
            # 이동 - removeRow ~ 
            for r in range(removeRow, 4, -1):
                for c in range(4):
                    grid[r][c] = grid[r-1][c]
        
        # 파란색 검사
        while True:
            canRemove, removeCol = removeBlue(grid)
            if canRemove == False: break
            score['blue'] += 1
            for c in range(removeCol, 4, -1):
                for r in range(4):
                    grid[r][c] = grid[r][c-1]
       
        # 3. 연한 캄 검사
        # 1) 초록색
        offset = 0
        for c in range(4):
            if grid[4][c] == 1:
                offset += 1
                break
        for c in range(4):
            if grid[5][c] == 1:
                offset += 1
                break 
        # 이동
        if offset > 0:
            for r in range(9, 5, -1):
                for c in range(4):
                    grid[r][c] = grid[r-offset][c]
        # 연한칸 비우기
        for c in range(4): 
            grid[4][c] = 0
            grid[5][c] = 0
        
        # 2) 파란색
        offset = 0
        for r in range(4):
            if grid[r][4] == 1:
                offset += 1
                break
        for r in range(4):
            if grid[r][5] == 1:
                offset += 1
                break
        # 이동
        if offset > 0:
            for c in range(9, 5, -1):
                for r in range(4):
                    grid[r][c] = grid[r][c-offset]
        # 연한칸 비우기
        for r in range(4):
            grid[r][4] = 0
            grid[r][5] = 0
        
    # 타일 개수
    greenTiles = [grid[r][c] for r in range(6, 10) for c in range(4) if grid[r][c] == 1]
    blueTiles = [grid[r][c] for r in range(4) for c in range(6, 10) if grid[r][c] == 1]
    
    print(score['green'] + score['blue'])
    print(len(greenTiles) + len(blueTiles))

solution()