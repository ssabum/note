import sys
sys.stdin = open("input.txt")

T = int(input())

def bubble(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

for tc in range(1, T+1):
    number = list(map(int, input().split()))

    bubble(number)

    number = number[1:9]

    tot = 0
    for i in number:
        tot += i
    ans = tot / len(number)

    ans = int(ans+0.5)
    
    print("#{} {}".format(tc, ans))

