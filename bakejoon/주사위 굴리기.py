def move(arr, dir):
    up, down, left, right, behind, front = arr
    if dir == 1:
        return [left, right, down, up, behind, front]
    elif dir == 2:
        return [right, left, up, down, behind, front]
    elif dir == 3:
        return [front, behind, left, right, up, down]
    elif dir == 4:
        return [behind, front, left, right, down, up]

def solution():
    n, m, r, c, k = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(n)]
    moveList = list(map(int, input().split()))

    dice = [0] * 6
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    
    for dir in moveList:
        nr = r + dr[dir-1]
        nc = c + dc[dir-1]
        
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        
        r, c = nr, nc
        
        # 주사위 업데이트
        dice = move(dice, dir)
        
        # 윗면 출력
        print(dice[0])
        
        # 아랫면 초기화
        if grid[r][c] == 0:
            grid[r][c] = dice[1]
        else:
            dice[1] = grid[r][c]
            grid[r][c] = 0

solution()
