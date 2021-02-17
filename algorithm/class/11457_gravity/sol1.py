import sys
sys.stdin = open("input.txt")

T = int(input())

# 각 위치별로 최대 중력을 찾는 함수
def check_gravity(numbers):
    # 최대 중력 0으로 초기화
    max_gravity = 0
    # 숫자들을 돌며
    for i in range(len(numbers)):
        # 만약 블럭이 없으면 통과
        if numbers[i] == 0:
            continue
        # 최대 중력치 설정
        my_gravity = len(numbers) - i - 1
        # 오른쪽의 블록들 확인(회전시 자기보다 긴 블록이 있을 경우 중력이 1씩 감소)
        for j in range(i+1, len(numbers)):
            if numbers[i] <= numbers[j]:
                my_gravity -= 1
        # 만약 각 위치의 중력들이 최대 중력보다 크면 갱신
        if my_gravity > max_gravity:
            max_gravity = my_gravity
    # 최대 중력값 리턴
    return max_gravity

for tc in range(1, T+1):

    length = input()
    numbers = list(map(int, input().split()))

    result = check_gravity(numbers)
    
    print("#{} {}".format(tc, result))

