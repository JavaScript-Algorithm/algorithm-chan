# x(열) y(행) d(시작방향) g(세대)
# 방향 - 0(동), 1(북), 2(서), 3(남)

# 끝점을 기준으로 시계방향 90도 회전 
# 0세대로 시작한다. [[x1, y1], [x2, y2]]

# 원점 기준 시계방향 90도 회전
# 1. x, y 교환
# 2. y축 * -1

# 기준점으로부터 90도 회전
# 1. 기준 좌표의 x,y를 빼준다
# 2. 회전 진행
# 3. 기준 좌표의 x,y를 더해준다


def rotate(last, coord):
    R, C = last
    r, c = coord

    r, c = r-R, c-C
    r, c = c, r
    c *= -1
    r, c = r+R, c+C
    return [r, c]

def solution():
    n = int(input())
    dragons = [list(map(int, input().split())) for _ in range(n)]
    grid = [[0] * 101 for _ in range(101)]
    move = [[0,1], [-1,0], [0,-1], [1,0]]
    for dragon in dragons:
        c, r, d, g = dragon
        nr, nc = r + move[d][0], c + move[d][1]
        coords = [[r, c], [nr, nc]]
        
        for _ in range(1, g+1):
            # [:-1]를 끝점을 기준으로 90도 회전하고, 이어붙인다
            last = coords[-1]
            rest = coords[:-1]
            rest.reverse()

            for coord in rest:
                coords.append(rotate(last, coord))
        
        # grid에 모든 점 반영
        for coord in coords:
            grid[coord[0]][coord[1]] = 1
    
    ans = 0
    for i in range(100):
        for j in range(100):
            if grid[i][j] == grid[i][j+1] == grid[i+1][j+1] == grid[i+1][j] == 1:
                ans += 1
    print(ans)

solution()