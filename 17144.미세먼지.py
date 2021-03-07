import sys
sys.stdin = open("test.txt", "r")
input = sys.stdin.readline
import copy
from collections import deque

r, c, t = map(int, input().split())
_map = []

# -1: 공기청정기 (항상 1열, 크기 2)
# 
for _ in range(r):
    _map.append(list(map(int, input().split())))

def spread():
    temp_map = copy.deepcopy(_map)

    q = deque()
    for x, row in enumerate(_map):
        for y, item in enumerate(row):
            if item>0:
                q.append((x, y))

    while q:
        p = q.pop()
        dust = _map[p[0]][p[1]] // 5
        count = 0
        
        # 상
        if 0 <= p[0]-1 < r and _map[p[0]-1][p[1]] != -1:
            count += 1
            temp_map[p[0]-1][p[1]] += dust
        # 하
        if 0 <= p[0]+1 < r and _map[p[0]+1][p[1]] != -1:
            count += 1
            temp_map[p[0]+1][p[1]] += dust
        # 좌
        if 0 <= p[1]-1 < c and _map[p[0]][p[1]-1] != -1:
            count += 1
            temp_map[p[0]][p[1]-1] += dust
        # 우
        if 0 <= p[1]+1 < c and _map[p[0]][p[1]+1] != -1:
            count += 1
            temp_map[p[0]][p[1]+1] += dust
        temp_map[p[0]][p[1]] -= dust*count

    return temp_map
        

def wind():
    temp_map = copy.deepcopy(_map)
    
    pure = None
    for x in range(r):
        if _map[x][0] == -1:
            pure = x
            break
    
    # 위쪽 청정기에서 뿜어져 나오는 부분
    before = 0
    for i in range(1, c):
        temp_map[pure][i] = before
        before = _map[pure][i]
    for i in range(pure-1, -1, -1):
        temp_map[i][c-1] = before
        before = _map[i][c-1]
    for i in range(c-2, -1, -1):
        temp_map[0][i] = before
        before = _map[0][i]
    for i in range(1, pure):
        temp_map[i][0] = before
        before = _map[i][0]

    # 아래 청정기에서 뿜어져 나오는 부분
    pure += 1
    before = 0
    for i in range(1, c):
        temp_map[pure][i] = before
        before = _map[pure][i]
    for i in range(pure+1, r):
        temp_map[i][c-1] = before
        before = _map[i][c-1]
    for i in range(c-2, -1, -1):
        temp_map[r-1][i] = before
        before = _map[r-1][i]
    for i in range(r-2, pure, -1):
        temp_map[i][0] = before
        before = _map[i][0]

    return temp_map

def remaining():
    result = 2
    for row in _map:
        result += sum(row)
    return result

while t > 0:
    _map = spread()
    _map = wind()
    t -= 1

print(remaining())