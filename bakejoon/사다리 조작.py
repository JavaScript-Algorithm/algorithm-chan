from itertools import combinations

def go(col, grid, n):
    row = 0

    # row보다 큰 모든 col열의 행을 탐색. 존재하지 않으면 종료
    while row < n:
        route = grid[row][col]
        row += 1
        if route == [0, 0]: continue
        if route == [1, 1]: return -1 # 양방향 다 길이 있음

        if route == [1, 0]: col -= 1    # 왼쪽
        elif route == [0, 1]: col += 1  # 오른쪽
        
    return col

def solution():
    m, k, n = list(map(int, input().split()))
    routes = [list(map(int, input().split())) for _ in range(k)]
    routes = list(map(lambda x: [x[0]-1, x[1]-1], routes))

    # 새로운 2차원 배열 생성 - [왼, 오]
    grid = [[[0, 0] for _ in range(m)] for _ in range(n)]

    # 모든 점선
    # (0, 0) ~ (n-1, m-2)
    allRoutes = [[a, b] for a in range(n) for b in range(m-1) if [a, b] not in routes]
    
    # 0~3개 선택
    for i in range(4):
        for addRoute in combinations(allRoutes, i):
            newRoute = list(addRoute) + routes        
            
            # newRoute 반영
            for a, b in newRoute:
                grid[a][b][1] = 1
                grid[a][b+1][0] = 1
            
            # 게임 시작
            flag = True
            for start in range(m):
                if start != go(start, grid, n):
                    flag = False
                    break
            if flag:
                return i
            
            # newRoute 해제
            for a, b in newRoute:
                grid[a][b][1] = 0
                grid[a][b+1][0] = 0
    return -1

print(solution())