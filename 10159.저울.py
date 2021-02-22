import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
import copy

_n = int(input()) # 5 ≤ N ≤ 100
_m = int(input()) # 0 ≤ M ≤ 2,000

_map = [ [ 0 for i in range(_n) ] for i in range(_n) ]
_map_reverse = copy.deepcopy(_map)

for _ in range(_m):
    _a, _b = map(int, input().split())
    _map[_a-1][_b-1] = 1
    _map_reverse[_b-1][_a-1] = 1

def do(map):
    for _x in range(_n):
        q = deque()
        for _y in range(_n):
            if map[_x][_y] == 1:
                q.append(_y)
        while q:
            new_x = q.pop()
            for new_y in range(_n):
                if new_y == _x: continue;
                if map[new_x][new_y] == 1 and map[_x][new_y] == 0:
                    map[_x][new_y] = 1
                    q.append(new_y)

do(_map)
do(_map_reverse)

_map = [[_x + _y for (_x, _y) in zip(x, y)] for (x, y) in zip(_map, _map_reverse)]

for row in _map:
    print(_n-1 - sum(row))