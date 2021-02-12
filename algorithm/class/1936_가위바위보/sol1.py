import sys
sys.stdin = open("input.txt")

# T = int(input())
#
#
# for tc in range(1, T+1):
#     num = list(map(int, input().split()))
#     print(num)
    
    # print("#{} ".format(tc, ))

A, B = map(int, input().split())

if A == 1 and B == 2:
    print("B")
elif A == 1 and B == 3:
    print("A")
elif A == 2 and B == 1:
    print("A")
elif A == 2 and B == 3:
    print("B")
elif A == 3 and B == 1:
    print("B")
else:
    print("A")