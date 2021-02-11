import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    N = int(input())
    numbers = input()
    num_dict = {}

    for num in numbers:
        if int(num) in num_dict:
            num_dict[int(num)] += 1
            continue
        num_dict[int(num)] = 1

    number = 0
    cnt = 0
    for idx, val in num_dict.items():
        if val > cnt:
            cnt = val
            number = idx
        if val == cnt:
            if number < idx:
                number = idx

    print("#{} {} {}".format(tc, number, cnt))

