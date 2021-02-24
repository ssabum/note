def combinations(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combinations(array[i + 1:], r - 1):
                yield [array[i]] + next

for i in combinations([1, 2, 3, 4], 3):
    print(i, end=" ")