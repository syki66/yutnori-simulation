

# 도 : 0.1536 (15.36%)
# 개 : 0.3456 (34.56%)
# 걸 : 0.3456 (34.56%)
# 윷 : 0.1296 (12.96%)
# 모 : 0.0256 (2.56 %)

# 앞면 : 1, 뒷면 : 0

# 앞면 : 40% , 뒷면 : 60% (평평한면이 위로 나올 확률이 높음)

import random

yut_p = [0, 0, 0, 0, 0]

count = 1000000
for _ in range(count):
    yuts = []
    for _ in range(4):
        yuts.append( random.choices(range(0,2), weights=[6,4])[0] )



    if yuts.count(0) == 1:
        yut_p[0] += 1
    elif yuts.count(0) == 2:
        yut_p[1] += 1
    elif yuts.count(0) == 3:
        yut_p[2] += 1
    elif yuts.count(0) == 4:
        yut_p[3] += 1
    else:
        yut_p[4] += 1


print(f'도 : {yut_p[0] / count}')
print(f'개 : {yut_p[1] / count}')
print(f'걸 : {yut_p[2] / count}')
print(f'윷 : {yut_p[3] / count}')
print(f'모 : {yut_p[4] / count}')