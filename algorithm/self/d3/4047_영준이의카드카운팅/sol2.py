import sys
sys.stdin = open("input.txt")

T = int(input())

pattern = {"S":0, "D":1, "H":2, "C":3}

for tc in range(1, T+1):
    line = input()

    card = [[0] * 14 for _ in range(4)]

    is_error = False
    for i in range(0, len(line), 3):
        # 패턴
        card_pattern = pattern[line[i]]
        # 번호
        card_num = int(line[i+1:i+3])
        # 해당카드 있으면 종료
        if card[card_pattern][card_num] == 1:
            is_error = True
            break
        # 아니라면 패턴 표시
        card[card_pattern][card_num] = 1
        # idx=0에 숫자 카운트
        card[card_pattern][0] += 1

    print("#{}".format(tc), end=" ")
    if is_error:
        print("ERROR")
    else:
        for i in range(4):
            print("{}".format(13-card[i][0]), end=" ")
        print()

