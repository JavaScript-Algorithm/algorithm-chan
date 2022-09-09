from collections import deque

def move(grid, dir, coord):
    moveList = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    r, c = coord 

    while True:
        nr = r + moveList[dir][0]
        nc = c + moveList[dir][1]
        
        # 구슬 만나는 경우
        if grid[nr][nc] == 'O':
            return [nr, nc]
        
        # 벽 만나는 경우
        if grid[nr][nc] == '#':
            return [r, c]
        r, c = nr, nc

def solution():
    # 입력값 받기
    n, m = list(map(int, input().split()))
    grid = [list(input()) for _ in range(n)]
    
    red = blue = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'R':
                red = [i, j]
            if grid[i][j] == 'B':
                blue = [i, j]
    
    q = deque([[red, blue, 0]])
    check = set()
    
    while len(q):
        front = q.popleft()
        redOrigin, blueOrigin, count = front 
        
        if count == 10:
            break
        
        for i in range(4):
            red, blue = redOrigin, blueOrigin
            redIsBig = False
            if i == 0 or i == 2:
                if red[0] > blue[0]:
                    redIsBig = True
                red = move(grid, i, red)
                blue = move(grid, i, blue)
                
                # 두 개의 좌표가 같은 경우
                if red == blue:
                    if grid[red[0]][red[1]] != 'O': 
                        if i == 0:
                            # 위로 이동
                            if redIsBig:
                                red = [blue[0] + 1, blue[1]]
                            else:
                                blue = [red[0] + 1, red[1]]
                        else:
                            # 아래로 이동
                            if redIsBig:
                                blue = [red[0] - 1, red[1]]
                            else:
                                red = [blue[0] - 1, blue[1]]
                                
            if i == 1 or i == 3:
                if red[1] > blue[1]:
                    redIsBig = True
                red = move(grid, i, red)
                blue = move(grid, i, blue)
                
                # 좌표 같은 경우
                if red == blue:
                    if grid[red[0]][red[1]] != 'O': 
                        if i == 1: 
                            # 오른쪽 이동
                            if redIsBig:
                                blue = [red[0], red[1] - 1]
                            else:
                                red = [blue[0], blue[1] - 1]
                        else:
                            # 왼쪽 이동
                            if redIsBig:
                                red = [blue[0], blue[1] + 1]
                            else:
                                blue = [red[0], red[1] + 1]
            
            # 큐에 추가
            if grid[red[0]][red[1]] == 'O' and grid[blue[0]][blue[1]] != 'O':                
                return count + 1
            if grid[red[0]][red[1]] != 'O' and grid[blue[0]][blue[1]] != 'O':
                hashKey = str(red[0]) + str(red[1]) + str(blue[0]) + str(blue[1])
                if hashKey not in check:
                    check.add(hashKey)
                    q.append([red, blue, count + 1])
            
    return -1
    
print(solution())