# 01.28_method 종류

---

> `python`에서 `instancemethod`, `staticmethod`, `classmethod`의 쓰임새를 알아보자🥴

## Class

> 클래스는 객체를 생성하고, 타입들이 가지는 공통적인 속성을 관리한다. 

## Instance method

>별도로 변수를 지정되어 있지 않아도, 호출을 하게 되면 인스턴스 변수를 찾아보고 클래스 변수를 찾아가게 된다.

## Class method

>`@classmethod`
>
>클래스 변수를 수정해야 하는 경우가 있다면 클래스 메서드로 정의 후 호출함으로써 변경
>
>해당 클래스에 속하는 모든 instance들에 공통적으로 변동사항이 발생 할 경우 사용

## Static method

>`@staticmethod`
>
>클래스와 연관은 있지만 인스턴스나 클래스가 가진 속성과 관계 없는 행동이 필요할때