#낚시왕이 오른쪽으로 한 칸 이동한다.
#낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
#상어가 이동한다.
# [s, d, z] = [속력, 이동방향, 크기]
# d =  위(0), 아래(1), 오른(2), 왼(3)

r, c, m = list(map(int, input().split()))
sharkInfo = [list(map(int, input().split())) for _ in range(m)]

def solution(n, m, sharkInfo):
    grid = [[0]*m for _ in range(n)]
    move = [[-1,0], [1,0], [0,1], [0,-1]]
    for r, c, s, d, z in sharkInfo:
        # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기
        grid[r-1][c-1] = [s, d-1, z]
    myFishSize = 0
    
    for myCol in range(m):
        # 1. 낚시왕 이동 완료
        # 2. 상어 잡기
        for r in range(n):
            if grid[r][myCol] != 0:
                s, d, z = grid[r][myCol]
                myFishSize += z
                grid[r][myCol] = 0
                break
        
        # 3. 상어 이동 
        # 1) 상어 위치 뽑기 
        sharkInfo = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    sharkInfo.append([i, j] + grid[i][j])
        
        # 2) grid 0으로 초기화
        grid = [[0]*m for _ in range(n)]

        # 3) 각 상어마다 위치 이동 - 위치 겹치면 크기가 큰 상어가 우선순위
        for r, c, s, d, z in sharkInfo:
            # d 방향으로 s만큼 이동
            # d =  위(0), 아래(1), 오른(2), 왼(3)

            if d in [0, 1]: rep = s % ((n-1)*2)
            else: rep = s % ((m-1)*2)

            for _ in range(rep):
                dr, dc = move[d]
                nr, nc = r + dr, c + dc
                
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    if d == 0: d = 1
                    elif d == 1: d = 0
                    elif d == 2: d = 3
                    elif d == 3: d = 2
                    dr, dc = move[d]
                    nr, nc = r + dr, c + dc
                r, c = nr, nc
            
            if grid[r][c] == 0 or (grid[r][c] != 0 and grid[r][c][2] < z):
                grid[r][c] = [s, d, z]

    print(myFishSize)
        
solution(r, c, sharkInfo)