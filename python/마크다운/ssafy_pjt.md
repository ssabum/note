## Project

> project를 위한 data collection

---

### Dictionary 데이터 요구사항

> 데이터를 가져오시오.

```python
import json

# 파일 열기
my_file = open('./music.json', encoding='utf-8')
# json 데이터를 python에서 사용하도록
music_dict = json.load(my_file)
print(music_dict)
```

> `singer`, `title` 데이터 가져와 `dict`로반환하는 함수를 만드시오.

```python
# 이쁘게 출력
import pprint

def music_info(music_dict):
    result = {}
    # 특정 데이터 가져오기
    singer = music_dict.get('singer')
    title = music_dict.get('title')
    # result에 데이터를 구조화
    result['singer'] = singer
    result['title'] = title

    return result
# 함수 실행 출력
print(music_info(music_dict))
```

---

###  List 데이터 요구사항

```python
import json

music_file = open('./music.json', encoding='utf-8')
music_list = json.load(music_file)

def music_info():
    result = []
    
    for music in music_list:
        info = {}
        singer = music.get('singer')
        title = music.get('title')
        info['singer'] = singer
        info['title'] = title
        # result.append(info)
        # list로 감싸지 않으면 key값만 들어가므로
        # list를 이용해 dict 전체를 넣어줌
        result += [info]
    return result

print(music_info(music_list))    
```