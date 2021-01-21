# Jupyter Notebook

> 웹 브라우저에서 파이썬 코드를 작성하고 실행하는 IDLE(통합개발환경)

* REPL(Read Eval Print Loop)로 파이썬 대화형 개발 환경 중 하나

* 셀 단위의 코드 실행으로 바로 결과를 확인 가능

* 마크다운 문법을 통해 풍부한 문서화 기능

`git bash here`에서 `pip install notebook`&`jupyter notebook`실행

| 단축키             | 내용                            |
| ------------------ | ------------------------------- |
| `b`                | 아래에 셀을 추가                |
| `a`                | 위에 셀을 추가                  |
| `ctrl`+`enter`     | 해당 셀을 실행                  |
| `shift`+`enter`    | 해당 셀을 실행하고 다음 셀 이동 |
| `h`                | 명령어 확인                     |
| `d`+`d`            | 셀 삭제                         |
| `c`                | 셀 복사                         |
| `x`                | 셀 잘라내기                     |
| `z`                | 셀 되돌리기                     |
| `m`                | 마크다운으로 변경               |
| `y`                | 코드로 변경                     |
| `ctrl`+`/`         | 주석                            |
| `ctrl`+`shift`+`-` | 셀 나누기                       |



### 주피터 노트북 & 확장 프로그램 삭제

* Git Bash 명령어 실행

  ```bash
  $ jupyter contrib nbextension uninstall --user
  $ pip uninstall jupyter_contrib_nbextensions
  $ pip uninstall notebook
  ```

* `.jupyter` 폴더 삭제

  * [jupyter 폴더 위치 찾기](https://ooyoung.tistory.com/7#:~:text=%EC%B2%98%EC%9D%8C%20%EC%A3%BC%ED%94%BC%ED%84%B0%20%EB%85%B8%ED%8A%B8%EB%B6%81%EC%9D%84%20%EC%8B%A4%ED%96%89,%EC%9D%B4%EB%A6%84%20%5D%EC%9C%BC%EB%A1%9C%20%EC%84%A4%EC%A0%95%EB%90%98%EC%96%B4%EC%9E%88%EB%8B%A4.)



### 주피터 노트북 & 확장 프로그램 설치

* Git Bash 명령어 실행

  ```bash
  $ pip install notebook
  $ pip install jupyter_contrib_nbextensions
  $ jupyter contrib nbextension install —user
  ```



### 주피터 노트북 실행 & 환경 설정

```bash
$ jupyter notebook
```

![image-20210119132258263](jupyter_notebook.assets/image-20210119132258263.png)



![image-20210119132406076](jupyter_notebook.assets/image-20210119132406076.png)
