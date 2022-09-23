from collections import deque
# 손님을 도착지로 데려다줄 때마다 연료가 충전
# 연료가 바닥나면 업무 끝
# 현위치 최단거리 손님 - 행번호, 열번호 작은 순서
# 연료는 한칸 이동마다 1 감소
# 손님 태워주면 - 목적지 이동까지 연료량 * 2배 충전

move = [[0,1], [0,-1], [1,0], [-1,0]]

def getMinGuest(grid, r, c, guest, n):
    # 방문 배열 생성
    visit = [[0] * n for _ in range(n)]
    filtGuest = list(map(lambda x: [x[0], x[1]], guest))
    candidates = []

    for i in range(len(filtGuest)):
        if filtGuest[i] == [r, c]:
            return [i, 0]

    for x, y in filtGuest:
        visit[x][y] = 2

    que = deque([[r, c, 0]])
    visit[r][c] = 1
    
    while len(que) > 0:
        x, y, dist = que.popleft()
        
        if len(candidates) > 0 and candidates[0][2] < dist:
            break
        
        for i in range(4):
            dx, dy = move[i]
            nx, ny = x + dx, y + dy 
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue 
            if grid[nx][ny] == 1 or visit[nx][ny] == 1: continue # 벽
            if visit[nx][ny] == 2:
                candidates.append([nx, ny, dist + 1])
            visit[nx][ny] = 1
            que.append([nx, ny, dist + 1])
    
    if len(candidates) == 0:
        return [-1, -1]
    candidates.sort(key=lambda x: (x[2], x[0], x[1]))
    x, y, dist = candidates[0]
    idx = filtGuest.index([x, y])
    return [idx, dist]

def goToDestination(grid, fromX, fromY, toX, toY, n):
    if fromX == toX and fromY == toY: return 0
    visit = [[0] * n for _ in range(n)]

    que = deque([[fromX, fromY, 0]])
    visit[fromX][fromY] = 1

    while len(que) > 0:
        x, y, dist = que.popleft()
        
        for i in range(4):
            dx, dy = move[i]
            nx, ny = x + dx, y + dy 
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue 
            if grid[nx][ny] == 1 or visit[nx][ny] == 1: continue # 벽
            if nx == toX and ny == toY:
                return dist + 1
            visit[nx][ny] = 1
            que.append([nx, ny, dist + 1])
    return -1

def solution():
    n, m, fuel = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(n)]
    start = list(map(lambda x: int(x) - 1, input().split()))
    guests = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    r, c = start

    for _ in range(m):
        # 1. 택시의 현재 위치에서 최단거리에 있는 손님을 구한다
        idx, dist1 = getMinGuest(grid, r, c, guests, n)

        if idx == -1: return -1

        fromX, fromY, toX, toY = guests[idx]
        guests = guests[:idx] + guests[idx+1:] #삭제

        fuel -= dist1
        if fuel < 0: return -1

        # 2. 목적지로 이동
        dist2 = goToDestination(grid, fromX, fromY, toX, toY, n)

        if dist2 == -1: return -1

        fuel -= dist2
        if fuel < 0: return -1

        # 3. 연료 채우기
        r, c = toX, toY
        fuel = fuel + dist2 + dist2
    return fuel

print(solution())