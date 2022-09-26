move = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]

def solution():
    N, M = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(N)]
    info = [list(map(int, input().split())) for _ in range(M)]
    info = list(map(lambda x: [x[0]-1,x[1]], info))
    clouds = [[N-1, 0], [N-1,1], [N-2,0], [N-2,1]]

    for d, cnt in info:
        cloudsInfo = [[0] * N for _ in range(N)]

        # 1. 구름 이동
        dx, dy = move[d]
        cnt = cnt % N
        for i in range(len(clouds)):
            # 음수면 -> N 더함
            # 양수면 -> %N
            x, y = clouds[i]
            x += (dx * cnt)
            y += (dy * cnt)
            if x >= N: x %= N
            if y >= N: y %= N 
            if x < 0: x += N
            if y < 0: y += N
            clouds[i] = [x, y]
        
        for x, y in clouds:
            cloudsInfo[x][y] = 1

        # 2. 구름에 위치한 바구니의 물의 양 + 1
        for x, y in clouds:
            grid[x][y] += 1
        
        # 3. 물이 증가한 칸에 물복사버그 마법 시전
        for x, y in clouds:
            # copyGrid에서 대각선 비교, 반영은 grid에
            # [x, y]의 대각선 중에 물이 있는 바구니 개수 구하기
            count = 0
            for i in [1,3,5,7]:
                dx, dy = move[i]
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if grid[nx][ny] != 0:
                    count += 1
            grid[x][y] += count
        
        # 4. 2 이상인 칸에 구름이 생기고, 물의 양이 2 줄어든다.
        #  단, 기존에 clouds에 있는 칸은 제외
        newClouds = []
        for r in range(N):
            for c in range(N):
                if grid[r][c] >= 2 and cloudsInfo[r][c] == 0:
                    newClouds.append([r, c])
                    grid[r][c] -= 2
        clouds = newClouds

    print(sum([grid[r][c] for r in range(N) for c in range(N) if grid[r][c] > 0]))

solution()