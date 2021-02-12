import sys
sys.stdin = open("input.txt")

T = int(input())

data = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def func(string):
    if not 0 <= int(string[:4]):
        return "-1"
    if not 1 <= int(string[4:6]) <= 12:
        return "-1"
    if not 1 <= int(string[6:]) <= data[int(string[4:6])]:
        return "-1"
    return string[:4]+'/'+string[4:6]+'/'+string[6:]

for tc in range(1, T+1):

    number = input()

    result = func(number)

    print("#{} {}".format(tc, result))

