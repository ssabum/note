import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # data: 학생 1000명의 점수 리스트
    # data의 각 원소는 0이상 100이하 정수
    data = list(map(int, input().split()))

    # 점수 빈도수 리스트
    score = [0 for _ in range(len(data)+1)]

    # data를 돌며 0~100점까지 해당 점수가 있으면 카운트 증가
    for i in data:
        score[i] += 1

    top = score[0]
    top_score = 0
    for i in range(len(score)):
        if score[i] >= top:
            top = score[i]
            top_score = i
    
    print("#{} {}".format(tc, top_score))

