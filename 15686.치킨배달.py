import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
import copy

_n, _m = map(int, input().split())
_map = []

for _ in range(_n):
    _map.append(list(map(int, input().split())))

_cost_map = []
_houses = []
_chiken = []

for _x in range(_n):
    for _y in range(_n):
        if _map[_x][_y] == 1:
            _houses.append((_x, _y))
        elif _map[_x][_y] == 2:
            _chiken.append((_x, _y))

def cal(start: set, end: set):
    return abs(start[0]-end[0]) + abs(start[1] - end[1])

for index in range(len(_chiken)- _m):
    for start in _houses:
        acc = float('inf')
        for _i in range(_m):
            acc += min(acc, cal(start, _chiken[index + _i]))
        _cost_map.append(acc)
        for one in range(len(_chiken) - 2):
            for two in range(one+1, len(_chiken) - 1):
                for three in range(two+1, len(_chiken)):
                    acc = 0
                    for start in _houses:
                        acc += min([cal(start, _chiken[one]), cal(start, _chiken[two]), cal(start, _chiken[three])])
                    _cost_map.append(acc)

print(min(_cost_map))