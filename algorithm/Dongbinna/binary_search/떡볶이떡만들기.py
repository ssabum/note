# 최적화 문제를 결정 문제(예 or 아니오)로 바꾸어 해결하는 기법
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

# 이진탐색을 위한 시작점과 끝점
start = 0
end = max(arr)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in arr:
        # 잘랐을때 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 왼쪽 부분 탐색
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 오른쪽 부분 탐색
    else:
        # 최대한 덜 잘렸을 때가 정답이므르 여기에 result 기록
        result = mid
        start = mid + 1

print(result)