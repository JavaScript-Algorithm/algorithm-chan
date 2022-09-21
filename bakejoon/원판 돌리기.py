from collections import deque 
# d: 0(시계), 1(반시계)

def getMult(x, N):
    ret = []
    tmp = x
    while x <= N:
        ret.append(x-1)
        x += tmp
    return ret

def solution():
    N, M, T = list(map(int, input().split()))
    board = [deque(map(int, input().split())) for _ in range(N)]
    rotateInfo = [list(map(int, input().split())) for _ in range(T)]

    # x: 판 번호, d: 방향, k: 회전 횟수
    for x, d, k in rotateInfo:
        # 1. x배수 판을 d 방향으로 k번 회전
        if d == 0: d = 1
        elif d == 1: d = -1
        rotateBlockNums = getMult(x, N)
        for i in rotateBlockNums:
            for _ in range(k):
                board[i].rotate(d)
        
        # 2. 모든 원소에 대해 인접하면서 수가 같은 것을 추출
        adjacents = []
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0: 
                    continue
                adj = [(i, j)]
                val = board[i][j] 

                # 음수는 그대로, 양수는 나머지로
                # 좌우는 공통 검사
                if board[i][(j+1) % M] == val:
                    adj.append((i, (j+1) % M))
                if board[i][j-1] == val:
                    adj.append((i, j-1))

                # i == 0인 경우 위만 검사
                if i == 0: 
                    if board[i+1][j] == val:
                        adj.append((i+1, j))

                # i == N-1인 경우 아만 검사
                elif i == N-1: 
                    if board[i-1][j] == val:
                        adj.append((i-1, j))

                # 그 외에는 위아 모두 검사
                else: 
                    if board[i+1][j] == val:
                        adj.append((i+1, j))
                    if board[i-1][j] == val:
                        adj.append((i-1, j))

                if len(adj) > 1:
                    adjacents += adj
        
        check = [board[i][j] for i in range(N) for j in range(M) if board[i][j] != 0]
        if len(check) == 0:
            print(0)
            return
        
        if len(adjacents) > 0:
            for i, j in adjacents:
                board[i][j] = 0
        else:
            nums = [board[i][j] for i in range(N) for j in range(M) if board[i][j] != 0]
            average = sum(nums) / len(nums)
            for i in range(N):
                for j in range(M):
                    if board[i][j] == 0: continue
                    if board[i][j] > average:
                        board[i][j] -= 1
                    elif board[i][j] < average:
                        board[i][j] += 1
        
    print(sum([board[i][j] for i in range(N) for j in range(M)]))

solution()