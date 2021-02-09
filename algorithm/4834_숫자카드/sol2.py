import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    a = input()
    how_many = {}

    for i in a:
        if int(i) in how_many:
            how_many[int(i)] += 1
            continue
        how_many[int(i)] = 1

    how = 0
    many = 0
    for i, v in how_many.items():
        if v > many:
            how = i
            many = v
        if v == many:
            if how < i:
                how = i


    print("#{} {} {}".format(tc, how, many))

