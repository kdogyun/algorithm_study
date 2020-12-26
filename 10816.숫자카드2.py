import sys
input = sys.stdin.readline

_ = input()
cards = {}
for i in list(input().rstrip().split()):
    if int(i) in cards:
        cards[int(i)] += 1
    else:
        cards[int(i)] = 1

_ = input()
for i in list(input().rstrip().split()):
    if int(i) in cards:
        print(cards[int(i)], end=' ')
    else:
        print(0, end=' ')