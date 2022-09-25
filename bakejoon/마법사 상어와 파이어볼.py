def checkDir(arr):
    isAllEven = isAllOdd = True
    for elem in arr:
        if elem % 2 != 0:
            isAllEven = False
        if elem % 2 == 0:
            isAllOdd = False
    return isAllEven or isAllOdd 

def solution():
    N, M, K = list(map(int, input().split()))
    ballsInfo = [list(map(int, input().split())) for _ in range(M)]
    # r, c, m(질량), s(속력), d(방향)
    move = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

    for _ in range(K):
        # 1. 이동
        newBall = [[[] for _ in range(N+1)] for _ in range(N+1)]
        for x, y, m, s, d in ballsInfo:
            dx, dy = move[d]
            nx, ny = x , y
            for _ in range(s):
                nx += dx
                ny += dy
                
                # n 초과시
                if nx > N: nx = 1
                if ny > N: ny = 1

                # 1 미만일 때
                if nx < 1: nx = N
                if ny < 1: ny = N
            
            newBall[nx][ny].append([m, s, d])
        
        ballsInfo = []

        # 2. 합치고 분해
        for i in range(1, N+1):
            for j in range(1, N+1):
                if len(newBall[i][j]) == 1:
                    m, s, d = newBall[i][j][0]
                    ballsInfo.append([i, j, m, s, d])
                if len(newBall[i][j]) >= 2:
                    balls = newBall[i][j]
                    # 질량합
                    newM = sum(list(map(lambda x: x[0], balls))) // 5

                    if newM > 0:
                        # 속력합
                        newS = sum(list(map(lambda x: x[1], balls))) // len(balls)

                        # 방향 검사
                        isAll = checkDir(list(map(lambda x: x[2],balls)))
                        if isAll:
                            ballsInfo.append([i, j, newM, newS, 0])
                            ballsInfo.append([i, j, newM, newS, 2])
                            ballsInfo.append([i, j, newM, newS, 4])
                            ballsInfo.append([i, j, newM, newS, 6])
                        else:
                            ballsInfo.append([i, j, newM, newS, 1])
                            ballsInfo.append([i, j, newM, newS, 3])
                            ballsInfo.append([i, j, newM, newS, 5])
                            ballsInfo.append([i, j, newM, newS, 7])
    print(sum(list(map(lambda x: x[2], ballsInfo))))
                    
    

solution()