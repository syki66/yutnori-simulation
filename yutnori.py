# 윷놀이 게임기, 통계적 확률 계산기

# 둥근면 : 1, 평평한면 : 0
# 둥근면 : 40% , 평평한면 : 60% (평평한면이 위로 나올 확률이 높음)

# 도 : 0.1536 (15.36%)
# 개 : 0.3456 (34.56%)
# 걸 : 0.3456 (34.56%)
# 윷 : 0.1296 (12.96%)
# 모 : 0.0256 (2.56 %)

import random

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

    return winning_count, play_count


print ( playYutnori(10, 1000) )