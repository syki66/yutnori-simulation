# 윷놀이 뽑기 기계 확률 계산기

# 자바스크립트로 변환하기

# 둥근면 : 1, 평평한면 : 0
# 둥근면 : 40% , 평평한면 : 60% (평평한면이 위로 나올 확률이 높음)

# 도 : 0.1536 (15.36%)
# 개 : 0.3456 (34.56%)
# 걸 : 0.3456 (34.56%)
# 윷 : 0.1296 (12.96%)
# 모 : 0.0256 (2.56 %)

import random
import math

def throwYuts():
    yuts = []
    for _ in range(4):
        yuts.append(random.choices(range(0, 2), weights=[6, 4])[0])
    return yuts

def checkYuts(yuts):
    if yuts.count(0) == 1:
        return 1
    elif yuts.count(0) == 2:
        return 2
    elif yuts.count(0) == 3:
        return 3
    elif yuts.count(0) == 4:
        return 4
    else:
        return 5

def playYutnori(destination, play_count):
    winning_count = 0
    for _ in range(play_count):
        player = 0
        while player == 0 or player % 5 != 0:
            yuts = throwYuts()
            player += checkYuts(yuts)
            if player > (destination * 5):
                winning_count += 1
                break
    return play_count, winning_count

for i in range(1, 11):
    try:
        try_count, success_count = playYutnori(i, 100000000)
        percentage = round(success_count / try_count * 100, 4)
        expectation = math.ceil(100 / percentage) * 1000
        print(f'{i}번 뽑기 -> 시도 : {try_count}, 성공 : {success_count}, 확률 : {percentage}%, 1개당 뽑기 금액 : {expectation}원')
    except ZeroDivisionError:
        print(f'{i}번 뽑기 -> 시도 : {try_count}, 성공 : 0, 확률 : 0%')

''' 100,000,000번 시뮬레이션 결과
1번 뽑기 -> 시도 : 100000000, 성공 : 61109030, 확률 : 61.109%, 1개당 뽑기 금액 : 2000원
2번 뽑기 -> 시도 : 100000000, 성공 : 36656997, 확률 : 36.657%, 1개당 뽑기 금액 : 3000원
3번 뽑기 -> 시도 : 100000000, 성공 : 22005018, 확률 : 22.005%, 1개당 뽑기 금액 : 5000원
4번 뽑기 -> 시도 : 100000000, 성공 : 13204470, 확률 : 13.2045%, 1개당 뽑기 금액 : 8000원
5번 뽑기 -> 시도 : 100000000, 성공 : 7928852, 확률 : 7.9289%, 1개당 뽑기 금액 : 13000원
6번 뽑기 -> 시도 : 100000000, 성공 : 4758115, 확률 : 4.7581%, 1개당 뽑기 금액 : 22000원
7번 뽑기 -> 시도 : 100000000, 성공 : 2854749, 확률 : 2.8547%, 1개당 뽑기 금액 : 36000원
8번 뽑기 -> 시도 : 100000000, 성공 : 1712346, 확률 : 1.7123%, 1개당 뽑기 금액 : 59000원
9번 뽑기 -> 시도 : 100000000, 성공 : 1028748, 확률 : 1.0287%, 1개당 뽑기 금액 : 98000원
10번 뽑기 -> 시도 : 100000000, 성공 : 616921, 확률 : 0.6169%, 1개당 뽑기 금액 : 163000원
'''