from collections import deque
# 올리는 칸 = 0
# 분기점 = n
# 끝점 = 2n-1
# 로봇 큐, 내구도 큐
# 내구도 감소 -> 로봇 올리거나 이동하거나

n, k = list(map(int, input().split()))
convey = deque(list(map(int, input().split())))
robots = deque([0]*n)
cnt = 1

while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 회전한다
    convey.rotate(1)
    robots.rotate(1)
    
    # 내리는 위치에 도달하면 즉시 내린다 
    robots[-1] = 0

    # 2. 올라온 로봇 순서대로 벨트 회전 방향으로 이동 가능하면 이동한다. 
    #    이동 불가능하면 가만히 있는다
    #    이동 조건: 이동하려는 칸에 로봇이 없고, 그 칸의 내구도 1 이상
    for i in range(n-2, -1, -1):
        if robots[i] == 1 and robots[i+1] == 0 and convey[i+1] >= 1:
            robots[i+1] = 1
            robots[i] = 0
            convey[i+1] -= 1
    
    # 내리는 위치에 도달하면 즉시 내린다 
    robots[-1] = 0

    # 3. 올리는 위치 칸의 내구도가 0이 아니면 올리는 위치에 로봇 올림
    if convey[0] > 0:
        robots[0] = 1
        convey[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 k개 이상이면 종료. 아니면 1로 돌아감
    if convey.count(0) >= k:
        print(cnt)
        break
    
    cnt += 1