# 윷놀이 게임기, 통계적 확률 계산기

# 도 : 0.1536 (15.36%)
# 개 : 0.3456 (34.56%)
# 걸 : 0.3456 (34.56%)
# 윷 : 0.1296 (12.96%)
# 모 : 0.0256 (2.56 %)

# 둥근면 : 1, 평평한면 : 0

# 둥근면 : 40% , 평평한면 : 60% (평평한면이 위로 나올 확률이 높음)

import random

count = 1000

winning_count = 0
for _ in range(count):

    player = 0

    while player == 0 or player % 5 != 0:

        yuts = []
        for _ in range(4):
            yuts.append(random.choices(range(0, 2), weights=[6, 4])[0])


        if yuts.count(0) == 1:
            player += 1
        elif yuts.count(0) == 2:
            player += 2
        elif yuts.count(0) == 3:
            player += 3
        elif yuts.count(0) == 4:
            player += 4
        else:
            player += 5

        if player > 50:
            winning_count += 1
            break

print(winning_count, count)
