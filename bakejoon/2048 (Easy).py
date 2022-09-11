from itertools import product

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

def shiftBlock(block):
    # 현재 위치 i 미만의 0 인덱스를 찾는다
    for i in range(len(block)):
        if block[i] != 0:
            idx = 0
            while idx < len(block):
                if block[idx] == 0:
                    break
                idx += 1
            if idx < i:
                block[i], block[idx] = block[idx], block[i]

def moveBlock(block):
    shiftBlock(block)
    
    flag = True
    for i in range(len(block)-1):
        if flag:            
            if block[i] == block[i+1]:
                block[i] += block[i+1]
                block[i+1] = 0
                flag = False
        else:
            flag = True

    shiftBlock(block)    

def moveBoard(board, moves):
    board2 = [x.copy() for x in board]

    for direction in moves:
        # board2의 block들을 방향에 따라 이동시킨다
        if direction == LEFT:
            for block in board2:
                moveBlock(block)
        if direction == RIGHT:
            for block in board2:
                block.reverse()
                moveBlock(block)
                block.reverse()
        if direction == UP:
            for c in range(len(board2)):
                newBlock = [board2[r][c] for r in range(len(board2))]
                moveBlock(newBlock)
                for r in range(len(board2)):
                    board2[r][c] = newBlock[r]
        if direction == DOWN:
            for c in range(len(board2)):
                newBlock = [board2[r][c] for r in range(len(board2))]
                newBlock.reverse()
                moveBlock(newBlock)
                newBlock.reverse()
                for r in range(len(board2)):
                    board2[r][c] = newBlock[r]

    return max([board2[i][j] for i in range(len(board2)) for j in range(len(board2))])

def solution():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    directions = [UP, RIGHT, DOWN, LEFT]
    ans = 0

    for moves in product(directions, repeat=5):
        ans = max(ans, moveBoard(board, moves))
    print(ans)

solution()