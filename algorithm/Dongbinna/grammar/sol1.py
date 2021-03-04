# 리스트에서 특정 값의 원소 모두 제거
arr = [1, 2, 3, 4, 5, 5]
remove_set = {3, 5}
result = [i for i in arr if i not in remove_set]
# [1, 2, 4]

# 리스트에서 특정 값의 원소 모두 제거2
score = [90, 85, 77, 65, 97]
chetting_list = {2, 4}
result_ = []
for i in range(len(score)):
    if i+1 in chetting_list:
        continue
    if score[i] >= 80:
        result_.append(i+1)
# [1, 5]번째 학생

# 람다활용
arr = [1, 2, 3, 4]
brr = [5, 6, 7, 8]
result__ = list(map(lambda a,b: a+b, arr, brr))
# [6, 8, 10, 12]