# Ssafy Note

> ssafy 과정에서 내가 모르거나 중요한 것들 총망라

---

## 1주차(21.01.18~01.22)

* 변수할당

```python
# 서로 할당된 값을 바꾸는 코드
x = 10
y = 100
x, y = y, x

# 임시 변수 활용
x = 10
y = 100
temp = x
x = y
y = temp
```

* 파이썬에서 표현할 수 있는 가장 큰 수

  > 오버플로우(overflow)
  >
  > 데이터 타입 별로 사용할 수 있는 메모리 크기가 제한
  >
  > 표현할 수 있는 범위를 넘어가면 출력되지 않는 현상, 즉 메모리가 넘치는 현상

> 임의 정밀도 산술(arbitrary-precision arithmetic)
>
> 파이썬에서 사용하는 형태로 기존 방식과 달리, 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태

```python
# 큰 수 출력
import sys
max_int = sys.maxsize
super_max = sys.maxsize * sys.maxsize

# 진수표현
binary_number = 0b10
octal_number = 0o10
decimal_number = 10
hexadecimal_number = 0x10
```

* 실수의 연산

```python
a = 3.5 - 3.12
b = 0.38
# 첫번째 비교 방법
abs(a-b) <= 1e-10

# 두번째 비교 방법
import sys
abs(a - b) <= sys.float_info.epsilon

# 세번째 비교 방법
import math
math.isclose(a, b)
```

* 문자열 출력

  > 문자열은 `+`연산자로 이어붙이고, `*`로 반복 가능

* String interpolation

```python
name = 'Cha'
score = 4.5
# %-formatting
print('Hello, %s' % name)

# str.format()
print('Hello, {}, 내 성적은 {}'.format(name, score))

# f-string
print(f'Hello, {name}, 내 성적은 {score}!')
# f-string 출력형식지정
import datetime
today = datetime.datetime.now()
print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}')
# f-string 연산
pi = 3.141592
print(f'원주율은 {pi:.4}. 반지름이 2일때 원의 넓이는 {pi*2*2}')
```

* `bool`타입

```python
# Flase 반환
0, 0.0, (), [], {}, '', None
```

* Sequence형 컨테이너

  > 데이터가 순서대로 나열된 형식
  >
  > > `리스트`, `튜플`, `레인지`, `문자형`, `바이너리`

```python
# sequence에 담긴 특정 원소 개수 확인
a = [1, 1, 2]
a.count(1)
```

* Non_sequence형 컨테이너

  > `set`, `dictionary`

* Immutable데이터

  > 변경 불가능 데이터
  >
  > > `리터럴`, `레인지`, `튜플`

* Mutable데이터

  > `리스트`, `dict`, `set`

* 반복제어

```python
# break(종료)
# n = 0, 1, 2까지만 출력
n = 0
while True:
    if n == 3:
        break
    print(n)
    n += 1
    
# continue(이후의 코드 실행하지 않고 다음 요소부터 수행)
# 홀수만 출력
for i in range(10):
    if i % 2 == 0:
        continue
    print(f'{i}는 홀수야!')
    
# else(반복문이 끝까지 수행된 이후 실행)
# break로 종료시 실행하지 않음
for i in range(3):
    print(i)
    if i == 100:
        break
else:
    print('else문 실행됨')
```

* 함수의 입력

  > 매개변수(parameter)
  >
  > >`func(x)`입력을 받아 함수 내부에서 활용할 `변수`

> 전달인자(argument)
>
> > `func(2)`실제로 전달되는 `입력값`

* 기본 인자값(Default Argument Values)

```python
# greeting2() 입력시 '익명, 안녕?' 출력
# 기본 인자값을 가지는 인자 다음에 기본 값이 없는 인자 사용 불가능
def greeting2(name='익명'):
    print(f'{name}, 안녕?')
```

* 가변 인자 리스트(Arbitary Argument Lists)

```python
def students(*args):
    return args
```

* 가변 키워드 인자(Arbitary Keyword Arguments)

```python
def my_dict(**kwargs):
    return kwargs
```

* 에러&예외 처리

```python
try:
    empty_list = [1, 2, 3, 4, 5]
    print(empty_list[8])
except IndexError as err: # IndexError 발생시
    print(f'{err}, 오류가 발생했습니다.')
else: # 다른 오류 발생시
    print('아무튼 오류가 발생했습니다.')
finally: # 반드시 수행해야하는 문장
    print('그래도 파일은 종료합니다.')
```

```python
# rasie 예외를 강제로 발생
def avg(scores):
    if len(scores) == 0:
        raise Exception('리스트 넣으시오.')
    return sum(scores) / len(scores)
```

---