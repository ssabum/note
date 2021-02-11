import sys
sys.stdin = open("input.txt")

N = int(input())

numbers = []

for i in range(1, N+1):
    numbers.append(i)

for i in numbers:
    string = str(i)
    for j in string:
        if ('3' in j) or ('6' in j) or ('9' in j):
            j = "-"



# for tc in range(1, T+1):
#
#     print("#{} ".format(tc, ))

