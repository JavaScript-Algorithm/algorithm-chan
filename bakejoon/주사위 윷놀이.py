from itertools import product
# 이동은 화살표 방향대로만
# 파란색 칸에서 출발하면 파란색 화살표 따른다

GOAL = 100

routeA = [(0,10), (0,13), (0,16), (0,19)]
routeB = [(1,20), (1,22), (1,24)]
routeC = [(2,30), (2,28), (2,27), (2,26)]

routeD = [(3,25), (3,30), (3,35), (3,40)]
Droute = routeD + [GOAL, GOAL, GOAL, GOAL, GOAL]

routeE = [(4,2*i) for i in range(21)] + [GOAL, GOAL, GOAL, GOAL, GOAL]
for i in range(len(routeE)):
    if i == 5: routeE[i] = (0, 10)
    elif i == 10: routeE[i] = (1, 20)
    elif i == 15: routeE[i] = (2,30)
    elif i == 20: routeE[i] = (3, 40)

Aroute = routeA + routeD + [GOAL]
Broute = routeB + routeD + [GOAL]
Croute = routeC + routeD + [GOAL]

horses = [0,1,2,3]

# 4C10 중복조합
def solution():
    dice = list(map(int, input().split()))
    ans = 0
    tmp = [[3, 0, 2, 3, 1, 0, 1, 1, 3, 1]]
    for horseLoc in product(horses, repeat=10):    
    #for horseLoc in tmp:
        score = 0
        horseInfo = [(4,0),(4,0),(4,0),(4,0)]
        
        for idx in range(len(horseLoc)):
            i = horseLoc[idx]
            if horseInfo[i] == GOAL: continue
            horse = horseInfo[i]
            move = dice[idx]
            
            # 주사위만큼 이동
            if horse in routeA:
                tmp = Aroute.index(horse)
                horse = Aroute[tmp + move]
            elif horse in routeB:
                tmp = Broute.index(horse)
                horse = Broute[tmp + move]
            elif horse in routeC:
                tmp = Croute.index(horse)
                horse = Croute[tmp + move]
            elif horse in routeD:
                tmp = Droute.index(horse)
                horse = Droute[tmp + move]
            else:
                tmp = routeE.index(horse)
                horse = routeE[tmp + move]
            
            # 이동한 칸과 horseInfo 비교
            if horse == GOAL:
                horseInfo[i] = horse
                continue
            
            if horse in horseInfo: break
            
            horseInfo[i] = horse
            score += horse[1]
            
        ans = max(ans, score)
    print(ans)

solution()