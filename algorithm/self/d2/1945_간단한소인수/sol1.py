import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 숫자는 2이상 10000000이하
    # 2**a * 3**b * 5**c * 7**d * 11**e
    number = int(input())

    # 계산을 편하게 하기 위해 딕셔너리 생성
    index = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}

    # 키값을 돌면서 나누어지면 카운트를 벨류값에 추가
    # 여러번 나누어지면 카운트수 증가
    for i in index.keys():
        while number % i == 0:
            index[i] += 1
            number = number // i

    # 값 출력을 위한 저장
    a = index[2]
    b = index[3]
    c = index[5]
    d = index[7]
    e = index[11]

    print("#{} {} {} {} {} {}".format(tc, a, b, c, d, e))

