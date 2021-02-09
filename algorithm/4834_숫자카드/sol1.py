import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    size = int(input())
    data = int(input())
    numbers = []

    while data % 10:
        numbers.append(data % 10)
        data = data // 10

    for i in range(len(numbers)-1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    number = []
    for i in range(len(numbers)-1):
        if numbers[i] != numbers[i+1]:
            number.append(numbers[i])

    print(number)



    
    # print("#{} ".format(tc, ))

