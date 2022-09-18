from collections import deque
# 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
# 나무 심고 시작 

def solution():
    # k년이 지난 후 살아남은 나무의 수
    n, m, k = list(map(int, input().split()))
    addNutrits = [list(map(int, input().split())) for _ in range(n)]
    treesInfos = [list(map(int, input().split())) for _ in range(m)]
    treesInfos = list(map(lambda x: [x[0]-1, x[1]-1, x[2]], treesInfos))
    trees = [[deque([]) for _ in range(n)] for _ in range(n)]
    nutrits = [[5]*n for _ in range(n)]
    move = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
 
    # 나무 추가
    for x, y, z in treesInfos:
        trees[x][y].append(z)

    for _ in range(k):
        # 1. 봄: 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다
        # 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다
        # 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
        for r in range(n):
            for c in range(n):
                newTree = deque([])
                deadTree = deque([])
                for t in trees[r][c]:
                    if nutrits[r][c] >= t:
                        newTree.append(t+1)
                        nutrits[r][c] -= t
                    else:
                        deadTree.append(t)
                trees[r][c] = newTree

                # 2. 여름: 봄에 죽은 나무가 양분으로 변한다
                # 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다(//)
                for t in deadTree:
                    nutrits[r][c] += (t // 2)
        
        # 가을: 나무 번식
        # 나이가 5의 배수여야 한다. 인접한 8개의 칸에 나이가 1인 나무가 생긴다 
        for r in range(n):
            for c in range(n):
                for tree in trees[r][c]:
                    if tree % 5 == 0:
                        for dr, dc in move:
                            nr, nc = r + dr, c + dc
                            if nr < 0 or nr >= n or nc < 0 or nc >= n: 
                                continue
                            trees[nr][nc].appendleft(1)
                
                # 겨울: 양분 추가
                nutrits[r][c] += addNutrits[r][c]
    
    # 살아남은 나무의 개수 구하기
    ans = 0
    for r in range(n):
        for c in range(n):
            ans += len(trees[r][c])
    
    print(ans)

solution()