# 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교 하여, 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘
def insert(a):
    for i in range(1, len(a)):
        while 0 < i and a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            i -= 1

    return a