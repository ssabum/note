# 행맨 게임 프로그램
# 리스트에 3개 이상의 단어를 추가
# 리스트에서 랜덤으로 1개의 단어를 선택
# 단어의 길이에 맞게 밑줄 출력
# 사용자로부터 1글자씩 입력을 받되, 단어에 입력값이 표함되면 'correct' 출력, 아니면 'worng'출력
# 매번 입력을 받을 때마다 현재까지 맞힌 글자들 표시
# 정답을 맞히면 'success' 출력 후 프로그램 종료

from random import *
words = ["apple", "banana", "orange"]
word = choice(words)

letters = "" # 사용자로부터 지금까지 입력받은 모든 알파벳

while True:
    succed = True
    print()
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succed = False
    print()
    print()
    
    if succed == True:
        break
        print("성공!!!")

    letter = input("문자를 입력하세요 : ") # 사용자 입력 받기
    if letter not in letters:
        letters += letter
    
    if letter in word:
        print("정답!")
    else:
        print("땡!")