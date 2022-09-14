# 극이 다르면 전파 및 회전 
# 극이 같으면 그대로
# 6번이 왼쪽, 2번이 오른쪽
# N(0), S(1)
# 방향이 1이면 시계, -1이면 반시계

from collections import deque

def rotateWheel(wheels, wheel, direc, LR):
    if LR == 0 and wheel == 0:
        return
    if LR == 1 and wheel == 3:
        return
    
    # 왼쪽 전파 및 회전
    if LR == 0:
        if wheels[wheel][6] != wheels[wheel-1][2]:
            rotateWheel(wheels, wheel-1, direc * -1, 0)
            wheels[wheel-1].rotate(direc * -1)

    # 오른쪽 전파 및 회전
    if LR == 1:
         if wheels[wheel][2] != wheels[wheel+1][6]:
                rotateWheel(wheels, wheel+1, direc * -1, 1)
                wheels[wheel+1].rotate(direc * -1)

def solution():
    wheels = [deque(input()) for _ in range(4)]
    k = int(input())
    moves = [list(map(int, input().split())) for _ in range(k)]
    moves = list(map(lambda x: [x[0] - 1, x[1]], moves))
    
    for wheel, direc in moves:
        # wheel 좌측 회전
        rotateWheel(wheels, wheel, direc, 0)

        # wheel 우측 회전
        rotateWheel(wheels, wheel, direc, 1)

        # wheel 회전
        wheels[wheel].rotate(direc)

    ans = 0
    point = [1,2,4,8]
    for i in range(4):
        if wheels[i][0] == '1':
            ans += point[i]
    
    print(ans)

solution()
