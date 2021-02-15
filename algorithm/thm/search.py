# def sequentialSearch(a, n, key):
#     i = 0
#     while i < n and a[i] != key:
#         i += 1
#     if i < n:
#         return i
#     else:
#         return -1

arr = [4, 9, 11, 23, 19, 7]

key = 2

for i in range(len(arr)):
    if key == arr[i]:
        print(i, "에 위치")
        break
else:
        print("못찾음")