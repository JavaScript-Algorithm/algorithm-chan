from itertools import combinations

def getPoint(matrix, team):
    # team에서 두 개를 뽑고 점수 계산
    point = 0
    for i, j in combinations(team, 2):
        point = point + matrix[i][j] + matrix[j][i]
    return point

def solution():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    teams = set([i for i in range(n)])
    ans = 1e9

    for teamA in combinations(teams, n // 2):
        teamA = set(teamA)
        teamB = teams - teamA 
        ans = min(ans, abs(getPoint(matrix, teamA) - getPoint(matrix, teamB)))

    print(ans)

solution()