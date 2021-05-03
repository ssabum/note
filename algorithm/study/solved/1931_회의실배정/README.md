# 1931번 회의실 배정
[문제 보러가기](https://www.acmicpc.net/problem/1931)

## 🅰 코드

```python
n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

# 람다함수 쓰는것 익숙해지기!!!
arr.sort(key=lambda x: (x[1], x[0]))

count = 0
end = 0
for i in range(n):
    if end <= arr[i][0]:
        count += 1
        end = arr[i][1]

print(count)

```

---


## ✅ 후기
* 문제에서 주어지는 입력값을 받은 다음 `lambda`함수를 사용해 `끝나는 시간`과 `시작하는 시간`순으로 두번 정렬해주면 금방 해결할 수 있는 문제이다.
* 새삼 느끼지만 `lambda`함수는 정말 간단하고 편리한 것 같다. 자주 사용하는 버릇을 들여야 겠다;;😮