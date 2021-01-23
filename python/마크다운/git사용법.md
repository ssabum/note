# Git

> 분산 버전 관리 시스템(DVCS)

코드의 History를 관리하는 도구로 개발된 과정을 볼 수 있으며 이전 버전을 보원하고 변경 사항을 비교, 분석 및 병합도 가능

## 0. 순서

> working directory
>
> > stage fixes(git add)
>
> staging area
>
> > commit(git commit)
>
> git directory(repository)
>
> > checkout the project

## 1. 준비

* 윈도우에서 git을 사용하기 위해서는 `git bash`를 설치한다.
* git을 활용하기 위해서 GUI 툴인 `source tree`,`github desktop`등을 활용할 수 있다.
* 초기 설치를 완료한 이후에 컴퓨터에 작성자(`author`) 정보를 등록한다.

```bash
# author 정보 등록
$ git config --global user.name {user name}
$ git config --global user.email {user email}

# author 정보 확인
$ git config --global --list
```



## 2. 로컬 저장소(Local Repository) 활용하기

### 2.1 저장소 초기화

```bash
$ git init
```

* `.git`폴더가 생성되며, 이 곳에 저장소의 git 관련된 모든 정보가 저장된다.
* git bash에 `master`라고 표시된다. 이는 현재 `master`라는 `branch`에 있다는 뜻이다.

### 2.2 `add`

작업공간(working directory)에서 변경된 사항을 커밋으로 기록하기 위해 `staging area`를 거쳐야 한다.

```bash
$ git add . # 현재 디렉토리
$ git add images/ # 특정 폴더
$ git add iu.jpg # 특정 파일
```

### 2.3 `commit`

`commit`은 이력을 확정짓는 명령어다. 해당 시점의 스냅샷을 기록한다.

`commit`시에는 반드시 메시지를 작성 해야하며, 메시지는 변경사항을 알 수 있도록 명확하게 작성한다.

```bash
$ git commit -m "스타트캠프 소스코드 추가"
```

`commit`이후에는 아래의 명령어를 통해 지금까지 작성된 이력을 확인한다.

```bash
$ git log
$ git log --oneline # 한 눈에 보기 쉽게 출력
```



## 3. 원격 저장소(Remote Repository) 활용하기

> 원격저장소 기능을 제공하는 서비스에는 `Github`,`Gitlab`등이 있다.

### 3.1 준비

* Github에 새로운 Repository생성

### 3.2 원격 저장소 등록

```bash
$ git remote add origin {github url}

# 서로다른 원격 저장소를 사용하기 위해 이름을 다르게 연결
$ git remote add github {github url}
$ git remote add gitlab {gitlab url}

$ git push github master
$ git push gitlab master
```

* 원격 저장소(`remote`)를 `origin`이라는 이름을 가진 `github url`을 등록한다.
* 등록된 원격 저장소 목록을 보기 위해 아래 명령어를 입력한다.

```bash
$ git remote -v
```

### 3.3 `Push`

```bash
$ git push origin master
```

* `origin`이라는 이름으로 설정된 원격 저장소에 `master`브랜치를 업로드
* 이후 변경사항이 생길때마다 `add`>`commit`>`push`순으로 작업을 수행



### 4. 기타

| 명령어 | 내용                                                         |
| ------ | ------------------------------------------------------------ |
| pull   | clone이후 변화된 내용을 다른 환경에서 받아올 때, git pull origin master |
| clone  | 새로운 환경에서 처음으로 원격에 저장된 내용을 가져올 때, git clone URL주소 |

