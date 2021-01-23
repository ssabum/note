# 01.22_Dictionary접근

---

## Dictionart접근하는 방식

`dict`에 접근하는 방식은 `[key]`를 사용하는 방법과 `.get()`함수를 사용하는 방식이 있다.

그렇다면 두가지 방식 중 어떤 방식이 더 효과적일까?

```python
# dictionary에 없는 value를 호출할 때
dict['key'] # 오류발생
dict.get('key') # None 출력
```

위와 같은 이유로 `.get()`을 사용하는 습관을 기르도록 하자...👍

