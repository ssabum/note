import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 문자열 입력
    data = input()
    # 빈 문자열 생셩
    tmp = ""
    # 입력된 문자열을 거꾸로 돌면서 빈 문자열에 저장
    for i in range(len(data)-1, -1, -1):
        tmp += data[i]
    # 결과값 변수
    ans = 0
    # 만약 입력 문자열과 거꾸로 문자열이 같으면 1, 다르면 0 결과 저장
    if data == tmp:
        ans = 1
    else:
        ans = 0
    
    print("#{} {}".format(tc, ans))

