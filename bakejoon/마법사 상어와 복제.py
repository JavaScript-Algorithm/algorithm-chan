from itertools import product
# 0. 모든 물고기 위치 및 방향 저장
# 1. 모든 물고기가 한 칸 이동한다. 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다
#   - 물고기는 이동할 수 있을 때까지 45도 반시계방향 회전한다
#   - 좌(0), 좌상(1), 상(2), 우상(3), 우(4), 우하(5), 하(6), 좌하(7)
# 2. 상어가 연속해서 3칸을 이동한다(4방위). 경유 중에 물고기 칸 있으면 물고기 제외 + 냄새 남긴다
#   - 지워지는 물고기가 많은 방향 우선순위
#   - 상(0), 좌(1), 하(2), 우(3) 가 빠른게 우선순위
# 3. 두번 전 물고기 냄새가 사라진다
# 4. 0번에서 저장한 물고기들 복제 실시

# 물고기 이동 정보
fishMove = [[0,-1], [-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1]]

# 상어 이동가능 조합들 (상, 좌, 하, 우)
sharkMoves = []
items = [[0,1,2,3] for _ in range(3)]
for a, b, c in product(*items):
    sharkMoves.append([a, b, c])
sharkMove = [[-1,0], [0,-1], [1,0], [0,1]]

def solution():
    M, total_count = list(map(int, input().split()))
    fishes = [list(map(int, input().split())) for _ in range(M)]
    smellGrid = [[0] * 4 for _ in range(4)]
    fishGrid = [[[] for _ in range(4)] for _ in range(4)]
    shark = list(map(int, input().split()))
    fishes = list(map(lambda x: [x[0]-1, x[1]-1, x[2]-1], fishes))
    shark[0] -= 1
    shark[1] -= 1

    for r, c, d in fishes:
        fishGrid[r][c].append(d)
    
    for _ in range(total_count):
        # 물고기 grid 1차원 배열로 정리
        fishes = []
        for r in range(4):
            for c in range(4):
                if len(fishGrid[r][c]) > 0:
                    for d in fishGrid[r][c]:
                        fishes.append([r, c, d])

        # 1. 모든 물고기 정보 저장
        copiedFish = [fish.copy() for fish in fishes]
        
        # 2. 모든 물고기가 한 칸 이동한다 - 물고기 냄새, 격자 벗어남, 상어면 불가능
        for i in range(len(fishes)):
            r, c, d = fishes[i]

            for _ in range(8):
                dr, dc = fishMove[d]
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
                    d = (d + 7) % 8
                    continue
                if smellGrid[nr][nc] != 0 or (nr == shark[0] and nc == shark[1]):
                    d = (d + 7) % 8
                    continue
                
                # 이동 가능한 경우 이동하고 break
                fishes[i] = [nr, nc, d]
                break
        
        # fishGrid 업데이트
        for r in range(4):
            for c in range(4):
                fishGrid[r][c] = []
        for r, c, d in fishes:
            fishGrid[r][c].append(d)
        
        # 3. 상어가 연속해서 3칸을 이동한다(4방위). 경유 중에 물고기 칸 있으면 물고기 제외 + 냄새 남긴다
        sharkMoveCandidates = [] # 상어 이동방향, 먹은 물고기 수
        for dirs in sharkMoves:
            count = 0
            r, c = shark 
            visit = [[0] * 4 for _ in range(4)]

            for i in range(len(dirs)):
                dr, dc = sharkMove[dirs[i]]
                r, c = r + dr, c + dc
                if r < 0 or r >= 4 or c < 0 or c >= 4:
                    break
                if visit[r][c] == 0:
                    count += len(fishGrid[r][c])
                    visit[r][c] = 1

                if i == len(dirs) - 1:
                    sharkMoveCandidates.append([dirs, count])
        
        # sharkMoveCandidates 정렬 후 첫번째 이동정보 사용
        sharkMoveCandidates.sort(key=lambda x: (-x[1], x[0][0], x[0][1], x[0][2]))
        
        dirs = sharkMoveCandidates[0][0]
        sr, sc = shark 
        for d in dirs:
            dr, dc = sharkMove[d]
            sr, sc = sr + dr, sc + dc
            if len(fishGrid[sr][sc]) > 0:
                smellGrid[sr][sc] = 3
                fishGrid[sr][sc] = []
        shark = [sr, sc]
        
        # 4. 두번 전 물고기 냄새가 사라진다
        for r in range(4):
            for c in range(4):
                if smellGrid[r][c] > 0:
                    smellGrid[r][c] -= 1

        # 5. 1번에서 저장한 물고기들 복제 실시
        for r, c, d in copiedFish:
            fishGrid[r][c].append(d)
    
    # 격자에 있는 물고기 수
    ans = 0
    for r in range(4):
        for c in range(4):
            if len(fishGrid[r][c]) > 0:
                ans += len(fishGrid[r][c])
    print(ans)

solution()