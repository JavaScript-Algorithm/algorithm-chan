# 말 중복 가능
# 1~K번 말을 올려놓고 시작. 이동방향은 4방위. 순서대로 이동
# 말 이동시 중복말 같이 이동
# 중복된 말이 4개가 생기면 종료


def changeDir(direction):
    if direction == 1: return 2
    if direction == 2: return 1
    if direction == 3: return 4
    if direction == 4: return 3

def getHorseList(horseBoard, r, c, i):
    idx = horseBoard[r][c].index(i)
    returnHorse = horseBoard[r][c][idx:]
    horseBoard[r][c] = horseBoard[r][c][:idx]
    return returnHorse

def solution():
    n, k = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(n)] # 그냥 체스판 검사용
    horses = [list(map(int, input().split())) for _ in range(k)] # 말 위치 정보
    horses = list(map(lambda x: [x[0]-1, x[1]-1, x[2]], horses))
    horseBoard = [[[] for _ in range(n)] for _ in range(n)] # 체스판 위에 말이 놓이는 정보 배열
    move = [0, [0,1],[0,-1],[-1,0],[1,0]] # 이동 배열
    info = [0,'R','L','U','D']
    turn = 0
    
    # 말 초기화
    # 행, 열의 번호, 이동 방향
    for i in range(len(horses)):
        r, c, d = horses[i]
        horseBoard[r][c].append(i)

    # 방향: 오(1), 왼(2), 위(3), 아(4)
    # 흰(0), 빨(1), 파(2)
    while turn < 1000:
        # 1~K번말 이동 
        turn += 1
        for i in range(len(horses)): 
            r, c, d = horses[i]
            dr, dc = move[d]
            nr, nc = r + dr, c + dc
            
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                d = changeDir(d)
                dr, dc = move[d]
                nr, nc = r + dr, c + dc
                horses[i][2] = d

                if board[nr][nc] == 2:
                    # 파란색인 경우 멈춘다
                    continue
           
            if board[nr][nc] == 2:
                # 파 - 방향 전환
                d = changeDir(d)
                dr, dc = move[d]
                nr, nc = r + dr, c + dc
                horses[i][2] = d

                if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
                if board[nr][nc] == 2: continue

            if board[nr][nc] == 0:
                # 흰
                # 1. 그대로 이동. 자기 위에 있는 말 동반, 말 있으면 위에 쌓임
                horseList = getHorseList(horseBoard, r, c, i)
                  
                # 2. 다음 위치에 쌓고, horseList번째 말들의 위치 또한 변경
                horseBoard[nr][nc] += horseList
                if len(horseBoard[nr][nc]) >= 4:
                    return turn
                for idx in horseList:
                    horses[idx][0] = nr
                    horses[idx][1] = nc
            elif board[nr][nc] == 1:
                # 빨 
                # 1. 빨간색인 경우 이동하고 쌓일때 reverse 해줌
                horseList = getHorseList(horseBoard, r, c, i)
                horseList.reverse()
                horseBoard[nr][nc] += horseList
                if len(horseBoard[nr][nc]) >= 4:
                    return turn
                for idx in horseList:
                    horses[idx][0] = nr
                    horses[idx][1] = nc
    return -1

print(solution())
