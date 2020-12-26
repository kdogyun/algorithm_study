import sys
input = sys.stdin.readline

for _ in range(int(input())):
    note1 = input()
    note1 = {}
    for i in list(input().split()):
        note1[i] = 0
    
    note2 = input()
    note2 = list(input().split())
    for x in note2:
        if x in note1:
            print(1)
        else:
            print(0)