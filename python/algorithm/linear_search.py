# 순서대로 처음부터 하나하나 검색하여 값을 찾는 것
import random

numlist = (1, 5, 7, 13, 50, 120, 300, 320, 400, 700)

for k in range(10):
    cntsum = 0
    for i in range(10000):
        rndnum = numlist[random.randint(0, 9)]
        for n in numlist:
            cntsum += 1
            if n == rndnum:
                break
    print(cntsum/10000)