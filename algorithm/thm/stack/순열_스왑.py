arr = [1, 2, 3]

N = len(arr)

def perm(idx):
    if idx == N:
        print(arr)

    else:
        for i in range(idx, N):
            # 순서 변경
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx+1)
            # 이후 반복을 위한 원상복귀
            arr[idx], arr[i] = arr[i], arr[idx]

perm(0)