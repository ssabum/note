arr = [1, 2, 3]

N = len(arr)

sel = [0] * N

# check: 10진수 정수
def perm(idx, check):
    if idx == N:
        print(sel)
        return

    for j in range(N):
        # j번째 원소를 활용을 했으면 사용 X
        if check & (1<<j): continue

        sel[idx] = arr[j]
        # 원상복구가 필요 없다
        perm(idx+1, check | (1<<j))

perm(0, 0)