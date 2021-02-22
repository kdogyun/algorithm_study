import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

_n = int(input())
_map = [ ]
for _i in range(_n):
    _map.append(list(map(int, input().split())))

_ans = [ [ 0 for i in range(_n) ] for i in range(_n) ]
for _i in range(_n):
    q = deque()
    q.append(_i)
    while q:
        _x = q.pop()
        for _j in range(_n):
            if _map[_x][_j] == 1 and _ans[_i][_j] == 0:
                _ans[_i][_j] = 1
                q.append(_j)

for row in _ans:
    for item in row:
        print(item, end=' ')
    print()