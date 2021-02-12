import sys
sys.stdin = open("input.txt")

a, b = map(int, input().split())

if a == 1:
    if b == 2:
        print("B")
    print("A")

if a == 2:
    if b == 3:
        print("B")
    print("A")

if a == 3:
    if b == 1:
        print("B")
    print("A")