from collections import deque
#아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.

# 시작 크기 = 2
# 1초에 동서남북 한칸 이동
# 작거나 같으면 지나갈 수 있음
# 작은 물고기만 먹을 수 있음
# 자신의 크기와 같은 수의 물고기를 먹을 때마다 1 증가

# 더 이상 먹을 수 있는 물고기가 없으면 종료
# 먹을 수 있는 물고기 1마리: 먹음
# 두마리 이상: 우선순위는 상 좌 (row, col) 순으로 정렬

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
shark = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            shark = [i, j]
            grid[i][j] = 0
          
def solution(grid, shark, n):
    time = count = 0
    size = 2
    move = [[1,0],[-1,0],[0,1],[0,-1]]

    while True:
        # 물고기 탐색
        i, j = shark
        visit = [[0] * n for _ in range(n)]
        que = deque([[i, j, 0]])
        visit[i][j] = 1
        fishes = []
        
        while len(que) > 0:
            x, y, dist = que.popleft()

            for dx, dy in move:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if visit[nx][ny] == 1:
                    continue

                # 먹을 수 있는지 확인
                if 0 < grid[nx][ny] < size:
                    fishes.append([nx, ny, dist + 1])
                if grid[nx][ny] in [size, 0]:
                    que.append([nx, ny, dist + 1])
                visit[nx][ny] = 1
        
        # 가장 작은 물고기 먹고, 위치 이동, size 증가
        if len(fishes) == 0:
            break
        else:
            fishes.sort(key=lambda x: (x[2], x[0], x[1]))
            x, y, dist = fishes[0]
            time += dist
            grid[x][y] = 0
            shark = [x, y]
            count += 1
            if count == size:
                size += 1
                count = 0
    print(time)

        
solution(grid, shark, n)