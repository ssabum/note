import sys
sys.stdin = open("input.txt")

# 1이상 1000이하의 정수
N = int(input())

# 몫, 나머지 리스트
quo = []
rem = []

for i in range(1, 1001):
    if N % i == 0:
        quo.append(N // i)
        rem.append(i)

arr = quo + rem

arr = set(arr)

arr = list(arr)

for i in range(len(arr)-1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in arr:
    print(i, end=" ")