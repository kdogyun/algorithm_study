import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
from itertools import combinations

_n, _m = map(int, input().split())
result = float('inf')
_houses = []
_chicken_houses = []

for _x in range(_n):
    _row = list(map(int, input().split()))
    for _y, _item in enumerate(_row):
        if _item == 1:
            _houses.append((_x, _y))
        elif _item == 2:
            _chicken_houses.append((_x, _y))

def cal(start: set, end: set):
    return abs(start[0]-end[0]) + abs(start[1] - end[1])

for _chickens in combinations(_chicken_houses, _m):
    _sum = 0
    for _house in _houses:
        _dis = float('inf')
        for _chicken in _chickens:
            _dis = min( _dis, cal(_house, _chicken))
        _sum += _dis
    result = min(result, _sum)

print(result)