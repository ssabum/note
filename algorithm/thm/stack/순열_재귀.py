arr = [1, 2, 3]

N = len(arr)
# 결과들이 저장될 리스트
sel = [0] * N
# 해당 원소를 이미 사용했는지 안했는지에 대한 체크
check = [0] * N

def perm(idx):
    # 만약 다 뽑아서 정리했다면
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:
                # 값을 사용
                sel[idx] = arr[i]
                # 사용했다는 표시
                check[i] = 1
                perm(idx+1)
                # 반복문을 위한 원상복구
                check[i] = 0

perm(0)