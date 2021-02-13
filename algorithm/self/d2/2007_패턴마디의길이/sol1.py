import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 각 문자열의 길이는 30, 마디의 최대 길이는 10
    data = input()
    ans = 0
    # 문자열을 두번째자리부터 돌면서
    for i in range(1, len(data)):
        # 첫번째 자리의 문자와 같으면
        if data[i] == data[0]:
            # 그 사이의 문자열과 다음의 문자열이 같으면
            if data[:i] == data[i:2*i]:
                # 길이를 저장
                ans = len(data[:i])
                break

    print("#{} {}".format(tc, ans))

