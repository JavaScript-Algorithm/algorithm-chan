# 위(1), 아(2), 왼(3), 오(4)

move = [0, [-1,0], [1,0], [0,-1], [0,1]]

def setSmell(shark, smell, n, k):
    for i in range(n):
        for j in range(n):
            if shark[i][j] != 0:
                smell[i][j] = [shark[i][j][0], k] # [번호, 시간]

def decreaseSmell(smell, n):
    for i in range(n):
        for j in range(n):
            if smell[i][j] != 0:     
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = 0

def moveShark(shark, sharkPrior, smell, n):
    tmp = [[[] for j in range(n)] for _ in range(n)]

    # 1. 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향 (smell == 0)
    for i in range(n):
        for j in range(n):
            if shark[i][j] == 0: 
                continue
            num, d = shark[i][j]
            
            flag = True
            for k in sharkPrior[num][d]:
                dx, dy = move[k]
                nx, ny = i + dx, j + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                if smell[nx][ny] == 0:
                    shark[i][j][1] = k
                    tmp[nx][ny].append(shark[i][j])
                    shark[i][j] = 0
                    flag = False 
                    break

            if flag:
                for k in sharkPrior[num][d]:
                    dx, dy = move[k]
                    nx, ny = i + dx, j + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                    if smell[nx][ny][0] == shark[i][j][0]:
                        shark[i][j][1] = k
                        tmp[nx][ny].append(shark[i][j])
                        shark[i][j] = 0
                        break
    # tmp 반영
    for i in range(n):
        for j in range(n):
            if len(tmp[i][j]) == 0:
                continue
            tmp[i][j].sort(key=lambda x: x[0])
            shark[i][j] = tmp[i][j][0]


def solution():
    N, M, k = list(map(int, input().split()))
    shark = [list(map(int, input().split())) for _ in range(N)] # 상어 번호
    smell = [[0] * N for _ in range(N)] # 냄새 정보
    sharkDir = [0] + list(map(int, input().split())) # 상어 방향

    # shark에 방향 추가
    # [상어 번호, 상어 방향]
    for i in range(N):
        for j in range(N):
            if shark[i][j] != 0:
                sharkNum = shark[i][j]
                shark[i][j] = [sharkNum, sharkDir[sharkNum]]

    # 각 상어별 우선순위
    # i번 상어의 3번 방향 우선순위
    # sharkPrior[i][3]
    sharkPrior = [0]
    for _ in range(M):
        # 우선순위는 위, 아래, 왼쪽, 오른쪽 순서
        sharkPrior.append([0] + [list(map(int, input().split())) for _ in range(4)])

    # 시작 - 냄새 뿌리기
    setSmell(shark, smell, N, k)
    time = 0
    while time < 1000:
        time += 1

        # 1. 상어 이동 - 중복 상어 존재하면 번호 작은게 우선순위
        moveShark(shark, sharkPrior, smell, N)

        # 2. 냄새 뿌리기
        setSmell(shark, smell, N, k+1)

        # 냄새 배열 시간 1씩 감소
        decreaseSmell(smell, N)

        # 3. 1번 상어만 남는지 확인
        findOne = False
        count = 0
        for i in range(N):
            for j in range(N):
                if shark[i][j] != 0:
                    count += 1
                    if shark[i][j][0] == 1:
                        findOne = True
        if count == 1 and findOne:
            print(time)
            return
    print(-1)

solution()