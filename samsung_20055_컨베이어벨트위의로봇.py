import sys
sys.stdin = open("test.txt", "r")

from collections import deque

n, k = map(int, input().split())
a = deque(map(int,input().split()))
step = 0

robots = deque([])
#0 카운트
while a.count(0) < k:
    step += 1

    #회전
    for i in range(len(robots)):
        robots[i] += 1
    #a.rotate(1)
    temp = a.pop()
    a.appendleft(temp)

    #N에 도달했으면 로봇 내리기
    if robots:
        if robots[0] >= n-1:
            robots.popleft()

    #로봇 이동
    for i in range(len(robots)):
        if i != 0 and robots[i-1] == robots[i] + 1:
            continue
        if a[robots[i]+1] != 0:
            a[robots[i]+1] -= 1
            robots[i] += 1

    #N에 도달했으면 로봇 내리기
    if robots:
        if robots[0] >= n-1:
            robots.popleft()

    #로봇 올리기
    if a[0] != 0:
        robots.append(0)
        a[0] -= 1

print(step)