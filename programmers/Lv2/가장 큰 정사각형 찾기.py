# 실패. 다른 사람 풀이 참고함
def solution(board):
    height = len(board)
    width = len(board[0])
    dp = [[0] * width for _ in range(height)]
    
    # 0행과 0열은 board 값으로 초기화
    for r in range(height): dp[r][0] = board[r][0]
    for c in range(width): dp[0][c] = board[0][c]
    
    # 1행 1열부터 다음을 검사
    # 현재가 board에서 1이면 좌,상,좌상 최소값 + 1로 갱신
    for r in range(1, height):
        for c in range(1, width):
            if board[r][c] == 1:
                dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
    
    return max([x for row in dp for x in row]) ** 2
    