# 비어있는 칸이면 다음을 검사
# 1. 인접칸에 좋아하는 학생 수 구하기
# 2. 인접칸 빈칸 개수
# 정렬 기준 -> 학생수 내림차순, 빈칸 개수 내림차순, 행, 열 오름차순

# 빈 칸이 아니면 continue

def solution():
    N = int(input())
    studentInfo = [list(map(int, input().split())) for _ in range(N*N)]
    grid = [[0] * N for _ in range(N)]
    move = [[0,1], [0,-1], [1,0], [-1,0]]
    
    for sNum, A, B, C, D in studentInfo:
        # 행, 열, 좋아하는학생수, 빈칸수
        seatInfo = []        
        for r in range(N):
            for c in range(N):
                if grid[r][c] != 0: 
                    continue
                like = blank = 0

                for i in range(4):
                    dr, dc = move[i]
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    
                    if grid[nr][nc] == 0:
                        blank += 1
                    else:
                        if grid[nr][nc] in [A, B, C, D]:
                            like += 1
                seatInfo.append([r, c, like, blank])
        seatInfo.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
        r, c = seatInfo[0][0], seatInfo[0][1]
        grid[r][c] = sNum
    
    ans = 0
    score = [0, 1, 10, 100, 1000]

    for r in range(N):
        for c in range(N):
            for stu in studentInfo:
                sNum, A, B, C, D = stu
                if grid[r][c] == sNum:
                    likes = [A, B, C, D]
                    break 
            like = 0
            
            for i in range(4):
                dr, dc = move[i]
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                if grid[nr][nc] in likes:
                    like += 1
            ans += score[like]
    print(ans)

solution()