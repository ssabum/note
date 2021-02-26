import sys
sys.stdin = open("input.txt")

# 비용을 계산하는 함수
def money(arr):
    summ = 0
    for i in range(len(arr)):
        summ += i * arr[i]
    return summ

T = int(input())

for tc in range(1, T+1):
    # N: 블록의 개수, 1이상 50이하
    # M1: 첫번째 탑 층수, 1이상 50이하
    # M2: 두번째 탑 층수, 1이상 50이하
    N, M1, M2 = map(int, input().split())
    data = list(map(int, input().split()))
    # data를 정렬, 무거운 순서
    sort_data = sorted(data)[::-1]
    # 탑 2개 생성
    top1 = [0]
    top2 = [0]

    # 첫번째 탑이 낮을 때
    if M1 < M2:
        idx = 0
        # 순서대로 저장
        while True:
            top1.append(sort_data[idx])
            top2.append(sort_data[idx+1])
            idx += 2
            # 낮은 탑이 다 찼으면 break
            if len(top1) == M1+1:
                break
        # 나머지 저장
        for i in range(idx, len(sort_data)):
            top2.append(sort_data[i])
    # 두번째 탑이 낮을 때 반복
    else:
        idx = 0
        while True:
            top2.append(sort_data[idx])
            top1.append(sort_data[idx+1])
            idx += 2
            if len(top2) == M2+1:
                break
        for i in range(idx, len(sort_data)):
            top1.append(sort_data[i])

    # 총 비용 저장
    result = money(top1) + money(top2)
    # 결과 출력
    print("#{} {}".format(tc, result))