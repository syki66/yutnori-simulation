# 윷놀이 기계 확률 계산하기

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
        try_count, success_count = playYutnori(i, 1000000)
        percentage = round(success_count / try_count * 100, 4)
        expectation = math.ceil(100 / percentage) * 1000
        print(f'{i}번 -> 시도 : {try_count}, 성공 : {success_count}, 확률 : {percentage}%, 1개당 뽑기 금액 : {expectation}원')
    except ZeroDivisionError:
        print(f'{i}번 -> 시도 : {try_count}, 성공 : 0, 확률 : 0%')