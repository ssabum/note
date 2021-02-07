# 02.07_CSS

---

> SSAFY Web과정 css수업에서 내가 모르는 것과 중요한 것 중심으로 정리!

## 가상클래스 선택자

```python
a:active{클릭했을 때}
a:hover{마우스를 위로 올렸을 때}
a:visited{방문했을 때}
a:link{방문안했을 때}
a:focus{포커스했을 때}
```

## 클래스 선택자

```python
#a {id 선택자}
.a {class 선택자}
a {tag 선택자}
>: 직계자식요소
+: 이웃한 형제요소
~: 이웃한 여러 형제요소
name.a: a class를 가진 name
*: 전체
name:first-child: 첫번째 자식 name
only-child: 자식이 하나만 있을 때
last-child: 마지막 자식
nth-child(n): 자식들 중 n번째
nth-last-child(n): 자식들 중 뒤에서 n번째
name:first-of-type: 첫번째 name
nth-of-type(n): n번째 등장(even, odd 가능)
only-of-type: 자기 자신만 존재할 때
last-of-type: 마지막
empty: 아무것도 가지고 있지 않을 때
not(): 괄호안에 지칭하는게 없을 때
```

## View크기

```python
px: 고정된 크기
em: 상위 요소에 비례해서 크기
rem: 최상위 요소에 비례해서 크기
vw / vh : viewport 화면의 크기에 비례
```

## Position

```python
static
relative
absolute
fixed
float: 띄우기 => clear: float무시하기
```

## Flex

```python
flex-direction: row / column: 정렬 방향
flex-basis: 크기
flex-grow: 컨테이너 채우기
flex-shrink: 윈도우 창 크기를 줄었을때 줄어드는 속성
justify: 메인축 정렬
align: 교차축 정렬
content: 축 기준 여러줄
items: 축 기준 한줄
self: 개별 요소
flex-wrap: items의 크기가 container를 넘어가면 줄바꿈
oreder: items의 순서 설정
```

## Column

```python
multi column
column-count: n: n개의 컬럼으로 분리
column-width: 200px: 200px의 크기에 맞춰 컬럼을 분리
column-gap: 간격 속성
column-rule-style: 간격 스타일
column-span: 컬럼 무시
```

## Background

```python
background-image: url(); 배경에 이미지 지정
background-repeat: no-repeat; 배경 이미지의 반복 여부를 설정
repeat / no-repeat
background-position: center; 기본값: 0% 0%
background-size: cover; 기본값: auto
cover: 긴 너비에 크기를 맞춤
contain: 짧은 너비에 크기를 맞춤
background-blend-mode: 배경색과 배경이미지간의 blend 속성
mix-blend-mode: 배경이미지와 적용 요소간의 blend 속성
```

## Display

```python
# block
한 영역을 차지하는 박스형태
height, width 지정 가능
margin, padding 지정 가능

# inline
컨텐츠 영역 만큼
height, width 명시 x
margin은 위아래 적용 x
padding은 시각적으로 적용되지만 위아래는 실제적으로 공간을 차지 x

# inline-block
줄바꿈이 이루어지지 않는다
height, width 지정 가능
지정하지 않은 경우 컨텐츠만큼 영역
```

## Margin-collapsing

```python

```

## Tip

```python
# content
div 의미없는 블록요소
span 의미없는 인라인요소

# 애니메이션 효과
transform + transition: transform 효과의 사용

# box-sizing
content-box: 기본값으로 설정
border-box: 테두리 기준으로 크기를 지정
initial: 기본값으로 설정
inherit: 부모 요소의 속성값을 상속

# 기본 스크롤바 명령어
::-webkit-scrollbar: 스크롤바
```



