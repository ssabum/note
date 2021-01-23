import random

numlist = (1, 5, 7, 13, 50, 120, 300, 320, 400, 700)

for k in range(10):
    cntsum = 0
    for i in range(10000):
        start = 0
        end = len(numlist) - 1
        key = int((start + end) / 2)
        v = random.randint(start, end)
        while True:
            cntsum += 1
            if numlist[key] == numlist[v] or start == end:
                break
            elif numlist[key] < numlist[v]:
                start = key + 1
                key = int((start + end) / 2)
            else:
                end = key - 1
                key = int((start + end) / 2)

    print(cntsum / 10000)