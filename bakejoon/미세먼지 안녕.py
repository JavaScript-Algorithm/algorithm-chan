def spreadDust(room, R, C):
    newRoom = [[0] * C for _ in range(R)]
    move = [[1,0],[-1,0],[0,1],[0,-1]]

    for r in range(R):
        for c in range(C):
            if room[r][c] == -1: 
                newRoom[r][c] = -1
                continue

            # 인접한 방향에 공기청정기가 있거나, 칸이 없으면 확산 x
            # 확산 양 room[i][j] // 5
            # 남은 양 room[i][j] - (room[i][j] // 5) * 확산 개수
            count = 0
            for dr, dc in move:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue
                if room[nr][nc] == -1:
                    continue
                count += 1
                newRoom[nr][nc] += room[r][c] // 5
            newRoom[r][c] += (room[r][c] - (room[r][c] // 5) * count)
    return newRoom
            

def solution():
    R, C, T = list(map(int, input().split()))
    room = [list(map(int, input().split())) for _ in range(R)]
    
    # 공기청정기 위치
    cleaner = []
    for r in range(R):
        if room[r][0] == -1:
            cleaner.append(r)

    for _ in range(T):
        # 1. 확산
        room = spreadDust(room, R, C)

        # 2. 공기청정기 작동
        # 1) 윗부분 작동
        cleanerR = cleaner[0]
        for r in range(cleanerR-1, 0, -1): room[r][0] = room[r-1][0]
        for c in range(0, C-1): room[0][c] = room[0][c+1]
        for r in range(0, cleanerR): room[r][C-1] = room[r+1][C-1]
        for c in range(C-1, 1, -1): room[cleanerR][c] = room[cleanerR][c-1]
        room[cleanerR][1] = 0

        # 2) 아랫부분 작동
        cleanerR = cleaner[1]
        for r in range(cleanerR+1, R-1): room[r][0] = room[r+1][0]
        for c in range(0, C-1): room[R-1][c] = room[R-1][c+1]
        for r in range(R-1, cleanerR, -1): room[r][C-1] = room[r-1][C-1]
        for c in range(C-1, 1, -1): room[cleanerR][c] = room[cleanerR][c-1]
        room[cleanerR][1] = 0

    print(sum([room[r][c] for r in range(R) for c in range(C) if room[r][c] not in [0, -1]]))

solution()