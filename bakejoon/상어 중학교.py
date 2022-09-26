move = [[1,0],[-1,0],[0,1],[0,-1]]

def gravity(grid, n):
    # 열 차례대로 증가, 끝행부터 시작, 빈칸(-2)인 경우에만 블록 떙김
    for c in range(n):
        for r in range(n-1, 0, -1):
            if grid[r][c] == -2:
                move_r = r-1
                while True:
                    if move_r < 0 or grid[move_r][c] == -1: 
                        break 
                    if grid[move_r][c] >= 0:
                        grid[r][c], grid[move_r][c] = grid[move_r][c], grid[r][c]
                        break
                    move_r -= 1

def rotate(grid, n):
    copyGrid = [block.copy() for block in grid]
    for r in range(n):
        for c in range(n):
            grid[n-c-1][r] = copyGrid[r][c]

def getCluster(grid, visit, bVisit, cluster, r, c, bNum, N):
    cluster.append([r, c])
    visit[r][c] = 1
    if grid[r][c] != 0:
        bVisit[r][c] = 1

    for i in range(4):
        dr, dc = move[i]
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if grid[nr][nc] in [0, bNum] and visit[nr][nc] == 0:
            getCluster(grid, visit, bVisit, cluster, nr, nc, bNum, N)

def solution():
    N, M = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(N)]
    ans = 0 

    while True:
        bVisit = [[0] * N for _ in range(N)]
        clusters = []
        for r in range(N):
            for c in range(N):
                if grid[r][c] > 0 and bVisit[r][c] == 0:
                    cluster = []
                    visit = [[0] * N for _ in range(N)]
                    getCluster(grid, visit, bVisit, cluster, r, c, grid[r][c], N)

                    if len(cluster) > 1:
                        # cluster에서 무지개 블록 개수 세기
                        # 기준 블록 탐색
                        rainbow = 0
                        standard = [1e9, 1e9]
                        for x, y in cluster:
                            if grid[x][y] == 0:
                                rainbow += 1
                            else:
                                if x < standard[0]:
                                    standard = [x, y]
                                if x == standard[0] and y < standard[1]:
                                    standard = [x, y]
                        clusters.append([cluster, rainbow, standard])
        
        if len(clusters) == 0:
            break
        
        clusters.sort(key=lambda x: (-len(x[0]), -x[1], -x[2][0], -x[2][1]))

        removeCluster = clusters[0][0]
        L = len(removeCluster)
        ans += (L * L)
        
        for x, y in removeCluster:
            grid[x][y] = -2
       
        gravity(grid, N)
        rotate(grid, N)
        gravity(grid, N)

    print(ans)

solution()