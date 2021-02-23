# 선택정렬은 최대값을 찾은 뒤에 이 값을 정해진 위치로 보내준다.
def select(a):
    for i in range(len(a)-1, 0, -1):
        max = 0
        for j in range(1, i+1):
            if a[j] > a[max]:
                max = j
        a[i], a[max] = a[max], a[i]

    return a