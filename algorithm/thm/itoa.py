# 정수형을 문자형으로 변환

def itoa(num):
    num_str = []
    while num != 0:
        r = num % 10
        num_str.append(chr(ord('0') + r))
        num = num // 10

    num_str = num_str[::-1]
    return ''.join(num_str)

print(itoa(1004))