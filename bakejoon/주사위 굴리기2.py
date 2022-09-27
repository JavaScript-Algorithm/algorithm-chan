from collections import deque
# 처음 방향은 동쪽
# 이동 - 칸점수 획득
# 아랫면 > 칸 : 방향을 90도 시계방향
# 아랫면 < 칸 : 반시계 방향 회전
# 아랫면 = 칸 : 방향 변화 x

# 동남서북
move = [[0,1],[1,0],[0,-1],[-1,0]]

def moveDice(dice, d):
    up, down, right, left, front, behind = dice
    if d == 0: # 동
        return [left, right, up, down, front, behind]
    if d == 2: # 서
        return [right, left, down, up, front, behind]
    if d == 1: # 북
        return [front, behind, right, left, down, up]
    if d == 3: # 남
        return [behind, front, right, left, up, down]

def getScore(grid, gridNum, x, y, N, M):
    visit = [[0] * M for _ in range(N)]
    que = deque([[x, y]])
    visit[x][y] = 1
    cnt = 1

    while len(que) > 0:
        r, c = que.popleft()

        for i in range(4):
            dr, dc = move[i]
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if visit[nr][nc] == 1:
                continue
            if grid[nr][nc] == gridNum:
                visit[nr][nc] = 1
                que.append([nr, nc])
                cnt += 1
    return cnt

def solution():
    N, M, K = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(N)]

    # up, down, right, left, front, behind
    dice = [1,6,3,4,2,5]
    x = y = d = ans = 0

    for _ in range(K):
        # 1. 이동
        nx, ny = x + move[d][0], y + move[d][1]
        if nx < 0 or nx >= N or ny < 0 or ny >=M:
            d = (d + 2) % 4
        x, y = x + move[d][0], y + move[d][1]

        # 주사위 굴리기
        dice = moveDice(dice, d)

        # 2. (x,y)에서 점수 획득
        score = getScore(grid, grid[x][y], x, y, N, M)
        ans += (score * grid[x][y])

        # 3. 방향 변경
        if dice[1] > grid[x][y]:
            d = (d + 1) % 4
        elif dice[1] < grid[x][y]:
            d = (d + 3) % 4
    print(ans)

solution()