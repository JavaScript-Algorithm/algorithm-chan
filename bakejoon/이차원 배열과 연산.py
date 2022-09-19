# r, c, k
# 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬
# 수, 횟수
# 연산 적용 후에는 크기가 변한다
# 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
# A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간을 구해보자.
# R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
# C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.

# 1. 0을 제외한 모든 숫자를 필터링한다
# 2. (숫자, 횟수) 배열을 구한다
# 3. 횟수, 숫자 순서로 정렬한다
# 4. 크기가 원래보다 크면 다른 행에 적용한다. 단, 100을 초과하면 뒤에는 버린다.
# 5. 크키가 원래보다 작거나 같으면 (원래 길이 - 구한 길이)만큼 0을 뒤에 추가한다

def getNewBlock(block):
    filtered = list(filter(lambda x: x != 0, block)) # 1
    nums = set(filtered)
    numCount = [] # 2
    for num in nums:
        numCount.append([num, block.count(num)])
    numCount.sort(key=lambda x: (x[1], x[0]))
    newBlock = [x for y in numCount for x in y]
    newBlock = newBlock[:100]
    return newBlock

def solution():
    row, col, k = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(3)]
    row -= 1
    col -= 1

    count = 0

    if row <= len(grid)-1 and col <= len(grid[0])-1:
        if grid[row][col] == k:
                print(count)
                return 
    
    while count < 100:
        count += 1
        # 1. 연산 판별
        R, C = len(grid), len(grid[0])
        if R >= C:
            # R 연산 적용
            maxRow = 0
            for i in range(R):
                newRow = getNewBlock(grid[i])
                grid[i] = newRow
                maxRow = max(maxRow, len(newRow))
            for i in range(R):
                if len(grid[i]) < maxRow:
                    for _ in range(maxRow - len(grid[i])):
                        grid[i].append(0)
                else:
                    for _ in range(len(grid[i]) - maxRow):
                        grid[i].append(0)
        else:
            # C 연산 적용
            for c in range(C):
                cols = [grid[r][c] for r in range(R)] # 열 뽑기
                newCol = getNewBlock(cols)
                if len(grid) < len(newCol):
                    for _ in range(len(newCol) - len(grid)):
                        grid.append([0 for i in range(len(grid[0]))])
                else:
                    for _ in range(len(grid) - len(newCol)):
                        newCol.append(0)
                # newCol 적용
                for r in range(len(newCol)):
                    grid[r][c] = newCol[r]
        
        if row > len(grid)-1 or col > len(grid[0])-1:
            continue
        if grid[row][col] == k:
            print(count)
            return 
    print(-1)
    # (0,2) 5

solution()