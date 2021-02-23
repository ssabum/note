import sys
sys.stdin=open("input.txt")


T= int(input())

for tc in range(1, T+1):
    zero_list=[0 for _ in range(10)] # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    numbers=input()# 667767, str
    it_is_baby_gin=0

    for i in numbers : #
        zero_list[int(i)]+=1 # [0, 0, 0, 0, 0, 0, 6, 0, 0, 0]

    for j in range(len(zero_list)):
        if zero_list[j] >=3:
            it_is_baby_gin+=1
            zero_list[j]-=3

    for k in range(len(zero_list)-2): # 123123 [0, 2, 2, 2, 0000]
        if zero_list[k] and zero_list[k+1] and zero_list[k+2]:
            it_is_baby_gin+=1
            zero_list[k]-=1
            zero_list[k+1]-=1
            zero_list[k+2]-=1

    if it_is_baby_gin >=2 :
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))


