import sys
sys.stdin=open("input.txt")


T = int(input())

for tc in range(1, T+1):
    zero_list = [0 for _ in range(10)]
    numbers = input()
    it_is_baby_gin = 0

    # 숫자 카운트 증가
    for i in numbers:
        zero_list[int(i)] += 1

    # 같은게 3개이면 + 1
    for j in range(len(zero_list)):
        # 만약 전부다 같아서 6이면 베이비진 = 2
        if zero_list[j] == 6:
            it_is_baby_gin = 2
            break
        
        if 3 <= zero_list[j] < 6:
            it_is_baby_gin += 1
            zero_list[j] -= 3

    # 만약 베이비진=2가 아니면
    if it_is_baby_gin != 2:
        # 연속해서 있는 경우 베이비진 + 1
        for k in range(len(zero_list)-2):
            # 만약 1231232인 경우
            if zero_list[k] == 2 and zero_list[k+1] == 2 and zero_list[k+2] == 2:
                it_is_baby_gin = 2
                break
            # 아닌 경우
            if 0 < zero_list[k] and 0 < zero_list[k+1] and 0 < zero_list[k+2]:
                it_is_baby_gin += 1
                zero_list[k] -= 1
                zero_list[k+1] -= 1
                zero_list[k+2] -= 1

    # 베이비진이 2면 1, 아니면 0 출력
    if it_is_baby_gin == 2:
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))


