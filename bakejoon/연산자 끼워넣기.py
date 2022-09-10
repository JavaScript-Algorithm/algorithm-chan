from itertools import permutations
import math

n = int(input())
numList = list(map(int, input().split()))
operatorsNum = list(map(int, input().split()))
operator = ['+', '-', '*', '/']
operators = []
for i in range(4):
    operators += [operator[i]] * operatorsNum[i]

minN, maxN = 1e9, -1e9

for oper in permutations(operators, len(operators)):
    num = numList[0]
    for i in range(1, len(numList)):
        if oper[i-1] == '+':
            num += numList[i]
        elif oper[i-1] == '-':
            num -= numList[i]
        elif oper[i-1] == '*':
            num *= numList[i]
        else:
            num /= numList[i]
            if num > 0:
                num = math.floor(num)
            elif num < 0:
                num = math.ceil(num)
    minN = min(minN, int(num))
    maxN = max(maxN, int(num))

print(maxN)
print(minN)