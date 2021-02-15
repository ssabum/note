# 달팽이 배열
data = [[0] * 5 for i in range(5)]  # 0이 5행5열로 들어가 있는 2차원 리스트
n = 0;
s = 1;
i = 0;
j = -1;
k = 5

while True:
    for p in range(1, k + 1):
        n += 1
        j += s
        data[i][j] = n
    # for 끝 ===================================================
    k -= 1
    if k <= 0:
        break
    for p in range(1, k + 1):
        n += 1
        i += s
        data[i][j] = n
        # for 끝 ===================================================
    s *= -1
# while 끝 ===================================================


# 2차원 리스트 출력하기
for i in range(len(data)):
    for j in range(len(data[0])):
        print('%3d' % data[i][j], end='')
    print()
