from itertools import combinations
def impossible(newRoute):
    # newRoute 원소 중에 a가 같고 b 차이의 절대값이 1인게 있으면 True
    a_s = list(set(map(lambda x: x[0], newRoute)))

    for a in a_s:
        sameA = list(filter(lambda x: x[0] == a, newRoute))
        if len(sameA) == 1:
            continue
        sameA.sort()
        for i in range(len(sameA)-1):
            if abs(sameA[i][1] - sameA[i+1][1]) == 1:
                return True

    return False 

def go(col, newRoute):
    row = -1
    
    while True:
        flag = True
        for a, b in newRoute:
            if row < a and (b == col or b + 1 == col):
                if b == col: col += 1
                else: col -= 1
                row = a
                flag = False
                break
        if flag:
            break
        
    return col

def solution():
    # h: 세로선마다 가로선을 놓을 수 있는 위치의 개수
    m, k, n = list(map(int, input().split()))
    routes = [list(map(int, input().split())) for _ in range(k)]
    routes = list(map(lambda x: [x[0]-1, x[1]-1], routes))

    # 모든 점선
    # (0, 0) ~ (n-1, m-2)
    allRoutes = [[a, b] for a in range(n) for b in range(m-1) if [a, b] not in routes]

    # 1~3개 선택
    for i in range(4):
        for addRoute in combinations(allRoutes, i):
            # addRoute + routes 에 연속 가로선 있는지 확인
            newRoute = list(addRoute) + routes
            if impossible(newRoute):
                continue
            newRoute.sort(key=lambda x: x[0])

            # 게임을 시작해본다
            flag = True
            for start in range(m):
                if start != go(start, newRoute):
                    flag = False
                    break
            if flag:
                return i
    return -1

print(solution())