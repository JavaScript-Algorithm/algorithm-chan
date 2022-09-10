from collections import deque

def changeDir(coord, direction):
    coords = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위, 오, 아, 왼
    idx = coords.index(coord)
    if direction == 'L':
        idx -= 1
        if idx == -1:
            idx = 3
        return coords[idx]
    else:
        return coords[(idx + 1) % 4]

def solution():
    n = int(input())
    k = int(input())
    grid = [[0]*n for i in range(n)]
    
    # 사과 위치 입력
    apples = [list(map(int, input().split())) for i in range(k)]
    for i, j in apples:
        grid[i-1][j-1] = 1
        
    L = int(input())
    
    # 이동 정보 입력
    moveInfo = deque(list(map(lambda x: (int(x[0]), x[1]), [input().split() for i in range(L)])))
    
    snake = deque([(0, 0)])
    time = 0
    move = (0, 1)
    
    while True:
        # 1. 시간 경과
        time += 1
        
        # 2. 머리 이동 (첫번째 원소)
        head_x, head_y = snake[0]
        head_x += move[0]
        head_y += move[1]
        
        # 벽에 부딪히면 게임끝
        if head_x < 0 or head_x >= n or head_y < 0 or head_y >= n:
            return time
            
        # 몸통 좌표 중에 몸이랑 일치하는게 있으면 게임 끝
        if (head_x, head_y) in snake:
            return time
        
        # 3. 꼬리 이동 (사과 먹으면 그대로, 사과 안먹으면 pop)
        if grid[head_x][head_y] == 1:
            grid[head_x][head_y] = 0
        else: 
            snake.pop()
        
        # 머리 위치 큐에 삽입
        snake.appendleft((head_x, head_y))
        
        # 방향 전환 큐에 원소 있으면 확인. 첫번째 값 확인
        if len(moveInfo) > 0:
            change_time, direction = moveInfo[0]
            if change_time == time:
                move = changeDir(move, direction)
                moveInfo.popleft()
            
print(solution())