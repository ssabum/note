import sys
sys.stdin = open("input.txt")

T = int(input())

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


for tc in range(1, T+1):
    # N 숫자열의 길이
    # data 숫자열 입력
    N = int(input())
    data = list(map(int, input().split()))

    bubble_sort(data)

    print("#{}".format(tc), end= " ")

    for i in data:
        print(i, end=" ")
    print()