import sys
sys.stdin = open("input.txt")

T = int(input())

def check_babygin(numbers):
    # counter = [0] * 10
    counter = [0 for _ in range(10)]

    is_babysin = 0

    for number in numbers:
        counter[number] += 1

    # for idx in range(len(counter)): => [2,2,2,2,2,2]일 경우 오류 발생
    idx = 0
    while idx < len(counter):
        # triplet check
        if counter[idx] >= 3:
            # 카드 3장 버리기
            counter[idx] -= 3
            is_babysin += 1
            continue

        # run check
        if idx < 8:
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                # 카드 3장 버리기
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
                is_babysin += 1
                continue

        # 베이비진 등장
        if is_babysin == 2:
            return 1
        idx += 1
    # 베이비진 없음
    if is_babysin != 2:
        return 0

for tc in range(1, T+1):
    numbers = list(map(int, input()))
    result = check_babygin(numbers)
    print("#{} {}".format(tc, result))

