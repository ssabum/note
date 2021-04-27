T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())
    # 탐색할 숫자 입력
    number = list(map(int, input().split()))
    number_list = input()
    # 각 숫자별로 카운트 수를 저장할 배열 생성
    count_list = []
    # 이진탐색 진행하며 카운트 저장
    for i in number:
        l = 1
        r = N
        cnt_i = 0
        while True:
            c = int((l+r)/2)
            cnt_i += 1
            if c == i:
                break
            elif c <= i:
                l = c
            else:
                r = c
        count_list.append(cnt_i)
    # 가장 낮은 탐색 수 추출
    minimum = min(count_list)
    # 추출된 카운터를 지니는 숫자를 탐색
    cnt = 0
    for i in count_list:
        if i == minimum:
            break
        else:
            cnt += 1
    num = number[cnt]

    print("#{}".format(TC), num, minimum)
