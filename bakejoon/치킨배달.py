# 빈칸, 치킨집, 집
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합
# 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.
# 빈 칸(0), 집(1), 치킨집(2)

# 치킨집을 M개 고르고 각각의 경우에 대해 도시의 최소 치킨 거리를 구한다

from itertools import combinations

def distance(house1, house2):
    return abs(house1[0] - house2[0]) + abs(house1[1] - house2[1])

def solution():
    n, m = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(n)]
    allChickens = [[i, j] for i in range(n) for j in range(n) if grid[i][j] == 2]
    ans = 1e9

    for chickens in combinations(allChickens, m):
        distSum = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    distSum += min([distance([i, j], chicken) for chicken in chickens])
        ans = min(ans, distSum)

    print(ans)

solution()