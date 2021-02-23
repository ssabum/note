import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, size = input().split()
    data = list(input().split())

    num_dict = {}
    for i in data:
        if i in num_dict:
            num_dict[i] += 1
        else:
            num_dict[i] = 1

    base = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = []
    for i in base:
        for _ in range(num_dict[i]):
            result.append(i)

    ans = ' '.join(result)

    print("#{}".format(tc))
    print("{}".format(ans))

