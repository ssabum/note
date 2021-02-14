import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N: 알파벳과 숫자쌍의 개수, 1이상 10이하
    # Ci: 주어진 알파벳, A~Z의 대문자
    # Ki: 연속된 개수, 1이상 20이하 정수
    # 문서의 너비는 10 고정
    N = int(input())

    # 전체 입력 데이터 저장
    data = []
    for i in range(N):
        Ci, Ki = input().split()
        for i in range(int(Ki)):
            data.append(Ci)

    print("#{}".format(tc))

    # 전체 데이터에서 10개씩 출력
    i = 0
    while True:
        for j in data[i:i+10]:
            print(j, end="")
        print()
        i += 10
        # 만약 data의 길이를 초과한다면 break
        if i > len(data):
            break


