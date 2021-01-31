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
  > > `리터럴`, `레인지`, `튜플`, `frozenset`

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

## 2주차(21.01.25~01.29)

* 재귀함수(Recursive function)

```python
# 피보나치 수열
def fib(n):
    # base case
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

* 조건표현식(Conditional expression)

```python
# 조건표현식(=삼항연산자)
true_value if <조건식> else false_value
```

* Comprehension

```python
# List comprehension
[출력표현식 for 요소 in 입력Sequence [if 조건식]]
[출력표현식 [if 조건식 else 조건식] for 요소 in 입력Sequence]
[출력표현식 for 요소 in 입력Sequence for 요소 in 입력Sequence]

# Set comprehension
{출력표현식 for 요소 in 입력Sequence [if 조건식]}

# Dictionary comprehension
{Key:Value for 요소 in 입력Sequence [if 조건식]}
```

* 스코프(Scope)

  >global scope: 코드 어디에서든 참조할 수 있는 공간
  >
  >local scope: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간
  >
  >global variable: 전역 스코프에 정의된 변수
  >
  >local variale: 로컬 스코프에 정의된 변수

* 이름규칙

>위에서 아래로 이동
>
>Local scope: 정의된 함수
>
>Enclosed scope: 상위 함수
>
>Global scope: 함수 밖 변수, `input`모듈
>
>Built-in scope: 파이썬에 내장된 함수

* Function method

```python
# str(변경x, 순서o, 순회o)
fine(n): n의 첫번째 위치 반환, 없으면 -1 반환
index(n): n의 첫번째 위치 반환, 없으면 오류
replace(old, new, [count]): 문자열 대체
strip(): 특정 문자 제거
split(): 특정 단위로 분할
''.join(): 구분자로 합쳐서 문자열로 반환
capitalize(): 맨앞만 대문자
title(): 공백이나 `이후 대문자
upper(): 대문자 변화
lower(): 소문자 변환
swapcase(): 대↔소문자 변환
isalpha(): 알파벳인지 boolean 반환
isascii(): 아스키문자인지 boolean 반환
isalnum(): 알파벳+숫자인지 boolean 반환
isdecimal(): 숫자인지 boolean 반환
isdigit(): 숫자의 변형까지 boolean 반환(제곱표현)
isnumeric(): 숫자로 해석되는 기호까지 boolean 반환(분수형태)
isidentifier(): 파이썬의 키워드인지 boolean 반환
isprintable(): 출력가능한지 boolean 반환
isspace(): 화이트스페이스인지 boolean 반환(공백, 탭)
islower(): 소문자인지 boolean 반환
isupper(): 대문자인지 boolean 반환
istitle(): 앞글자만 대문자인지 boolean 반환
```

```python
# list(변경o, 순서o, 순회o)
append(): 리스트에 추가
extend(): 리스트에 확장(list, range, tuple, str 추가)
    cafe = ['starbucks', 'tomntoms', 'hollys']
    cafe.extend('ediya')
    print(cafe) # ['starbucks', 'tomntoms', 'hollys', 'e', 'd', 'i', 'y', 'a']
insert(n, x): 위치 n에 x를 삽입 # 맨뒤에 넣을 때는 n = len(원본) 사용
remove(): 삭제 없으면 오류
pop(n): 위치 n을 반환하며 원본에서 삭제
clear(): 모든 항목 삭제
index(n): n을 찾아 해당 index 반환
count(n): n의 개수 출력
sort(): 정렬 # sorted()와 다르게 원본 변형 후 None 반환
reverse(): 반대로 뒤집어서 출력
```

```python
# set(변경o, 순서x, 순회o)
add(): 세트에 추가
update(): 세트에 확장 # literable(순환가능) 추가
remove(): 삭제 없으면 오류
discard(): 삭제 없으면 오류x
pop(): 임의의 원소를 반환하며 원본에서 제거
```

```python
# dict(변경o, 순서x, 순회o)
get(key, n): value 반환, 없을 경우 n 반환
pop(key, n): value 반환하며 원본에서 제거, 없을 경우 n 반환
update({key: value}): 원본에서 덮어쓰기
keys(): keys 반환
values(): values 반환
items(): keys, values 반환
```

* 객체(Object)

  > `type`: 공통된 속성과 조작법을 가진 객체들의 분류
  >
  > `attribute`: 객체의 상태 / 데이터
  >
  > `method`: 특정 객체에 적용할 수 있는 행위

```python
# instance
# 특정 type의 실제 데이터 예시
# instancemethod는 호출시 첫번째 인자로 자기자신

# class
# 객체들의 분류를 정의할 때 쓰이는 키워드, 공통된 속성과 행위를 정의(사용자 정의 데이터형)
```

* 상속

  > 추상클래스: 무언가를 확립되지 않고 추상적으로 사용되는 클래스
  >
  > > 인스턴스 생성 x
  > >
  > > 자식 클래스들이 각각의 독립된 공통적인 기능을 갖출 때 사용
  > >
  > > 각각의 독립된 공통적인 기능이 값을 공유하면 안되므로 구현하지 않은 빈 메소드를 사용
  >
  > 다중상속: 여러 부모 클래스들로부터 상속 받는 것
  >
  > 메서드 오버라이딩: 부모클래스에서 정의된 메소드를 자식 클래스에서 다시 정의

```python
# super function
# 상속받은 부모 클래스를 의미
super().__init__(nmae)
```

* Map, Filter, Zip function

```python
# map
# iterable 객체의 모든 element에 함수를 적용한 후 return
map(function, iterable)

# filter
# iterable 객체의 모든 element에 함수를 적용한 후 True에 해당하는 element만 return
filter(function, iterable)

# zip
# 여러개의 iterable의 element를 하나씩 매핑하여 각각의 tuple로 병합
zip(*iterable)
```

