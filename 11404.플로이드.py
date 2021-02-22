import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

_n = int(input())
_m = int(input())

_map = [ [ float('inf') for i in range(_n) ] for i in range(_n) ]
for _ in range(_m):
    a, b, c = map(int, input().split())
    if _map[a-1][b-1] > c:
        _map[a-1][b-1] = c
    
for _x in range(_n):
    q = deque()
    for _y in range(_n):
        if _map[_x][_y] != float('inf'):
            q.append((_y, _map[_x][_y]))
    while q:
        (new_x, c) = q.pop()
        for new_y in range(_n):
            if new_y == _x: continue;
            if _map[new_x][new_y] != float('inf') and c + _map[new_x][new_y] < _map[_x][new_y]:
                _map[_x][new_y] = c + _map[new_x][new_y]
                q.append((new_y, _map[_x][new_y]))

for row in _map:
    for item in row:
        if item == float('inf'): item = 0;
        print(item, end=' ')
    print()