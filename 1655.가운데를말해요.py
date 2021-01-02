import sys
sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

nums = []
length = 0
for _ in range(int(input())):
    nums.append(int(input()))
    nums.sort()
    length += 1

    if length % 2 == 0:
        print(min( nums[ int(length/2)-1 ], nums[ int(length/2) ] ))
    else:
        print(nums[ int(length/2) ])