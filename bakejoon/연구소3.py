from itertools import combinations 
from collections import deque
# 0은 빈 칸, 1은 벽, 2는 바이러스의 위치
# 연구소 바이러스 M개를 활성 상태로 변경하려고 한다

# 값이 2인 좌표 추출
# m개의 조합마다 검사 실시
# bfs 너비가 1 증가할때마다 빈칸 개수 검사

def solution():
    n, m  = list(map(int, input().split()))
    gridO = [list(map(int, input().split())) for _ in range(n)]
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    
    # 0 이 없는 경우
    blanksO = len([0 for i in range(n) for j in range(n) if gridO[i][j] == 0])

    if blanksO == 0:
        return 0

    # 바이러스 위치 추출
    viruses = [[i, j] for i in range(n) for j in range(n) if gridO[i][j] == 2]

    # 벽은 -1, 바이러스는 -2로 설정
    for i in range(n):
        for j in range(n):
            if gridO[i][j] == 1:
                gridO[i][j] = -1
            elif gridO[i][j] == 2:
                gridO[i][j] = -2 
    
    ans = []

    # bfd
    for virus in combinations(viruses, m):
        # grid 초기화
        grid = [x.copy() for x in gridO]

        # 선정된 바이러스의 위치에 1 대입
        for i, j in virus:
            grid[i][j] = 1
        
        blanks = blanksO
        que = deque(list(virus))
        observe = 1

        while len(que) > 0:
            x, y = que.popleft()
            
            if grid[x][y] == observe + 1:
                if blanks == 0:
                    ans.append(observe)
                    break
                observe += 1
            
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                if grid[nx][ny] not in [0, -2]: continue
                if grid[nx][ny] == 0: blanks -= 1
                grid[nx][ny] = grid[x][y] + 1
                que.append([nx, ny])

    if len(ans) == 0: 
        return -1
    else: 
        return min(ans)    

print(solution())