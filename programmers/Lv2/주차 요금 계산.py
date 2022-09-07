import math

def toMin(time):
    hour, minute = time.split(':')
    return int(hour) * 60  + int(minute)
    
def solution(fees, records):
    # fees: 기본시간, 기본요금, 단위시간, 단위요금
    # records원소를 쪼개고, 차량번호를 key로 해서 시간을 분으로 변환해서 push한다
    # 각 key별로 배열의 길이가 홀수면 마지막에 23:59를 분으로 변환해서 push 해준다
    # 각 차량번호별로 요금을 계산해준다
    baseTime, baseFee, perTime, perFee = fees
    
    carHash = {}
    
    for record in records:
        time, car, inOut = record.split(' ')
        carHash.setdefault(car, [toMin(time)])
        carHash[car].append(toMin(time))
    
    ans = {}
    for car in carHash.keys():
        if len(carHash[car]) % 2 == 1:
            carHash[car].append(toMin('23:59'))
        
        # 요금 구하기
        timeSum = sum([carHash[car][i+1] - carHash[car][i] for i in range(0, len(carHash[car]), 2)])
        totalFee = baseFee + math.ceil((timeSum - baseTime) / perTime) * perFee
        if timeSum <= baseTime:
            totalFee = baseFee
        ans.setdefault(car, totalFee)
    
    # (car, fee)
    return list(map(lambda x: x[1], sorted(ans.items(), key=lambda x: x[0])))