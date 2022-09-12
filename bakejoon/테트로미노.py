# block을 시계방향으로 90도 회전시킨 블록을 반환
def rotate(block):
    # 행*열 -> 열*행
    n, m = len(block), len(block[0])
    newBlock = [[0]*n for _ in range(m)]
    
    for c in range(m):
        for r in range(n-1, -1, -1):
            newBlock[c][n-r-1] = block[r][c]
    
    return newBlock

def solution():
    n, m = list(map(int, input().split()))
    tmp = [list(map(int, input().split())) for _ in range(n)]
    board = [[0]*(m+8) for _ in range(n+8)]
    ans = 0

    for i in range(n):
        for j in range(m):
            board[i+4][j+4] = tmp[i][j]

    blocks = [[[1,1,1,1]],         # ㅡ
              [[1,1],[1,1]],       # ㅁ
              [[1,0],[1,0],[1,1]], # ㄴ
              [[0,1],[0,1],[1,1]], # ㄴ 대칭
              [[1,0],[1,1],[0,1]], # H
              [[0,1],[1,1],[1,0]], # H 대칭
              [[1,1,1],[0,1,0]]]   # ㅜ
    
    for blockNum, block in enumerate(blocks):
        for i in range(4):
            if blockNum == 0 and i == 2:
                break
            if blockNum == 1 and i == 1:
                break

            bn, bm = len(block), len(block[0])
            
            for r in range(n+8-bn):
                for c in range(m+8-bm):
                    tmpSum = 0
                    for br in range(bn):
                        for bc in range(bm):
                            if block[br][bc] == 1:
                                tmpSum += board[r+br][c+bc]
                    ans = max(ans, tmpSum)

            block = rotate(block)
    
    print(ans)

solution()
