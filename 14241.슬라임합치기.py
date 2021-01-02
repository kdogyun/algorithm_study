import sys
sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

#최대 힙으로 접근!
#힙 구현하기 귀찮으니 list와 sort로 구현해보자.

n = int(input())
slimes = list(map(int, input().rstrip().split()))
result = 0
while len(slimes) > 1:
    slimes.sort()
    one = slimes.pop()
    two = slimes.pop()
    result += one * two
    slimes.append(one + two)

print(result)