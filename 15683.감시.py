import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
import copy

xM, yM = map(int, input().split())
_map = []
result = float('inf')

for _ in range(xM):
    _map.append(list(map(int, input().split())))

def blind_spot(temp_map):
    count = 0
    for row in temp_map:
        for item in row:
            if item == 0:
                count += 1
    return count

# CCTV MAX 8개
cctv_list = []
for row_i, row in enumerate(_map):
    for item_i, item in enumerate(row):
        if 0 < item < 6:
            cctv_list.append((item, (row_i, item_i)))

one = [[(1, 0)], [(0, 1)], [(0, -1)], [(-1, 0)]]
two = [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]]
three = [[(1, 0), (0, 1)], [(1, 0), (0, -1)], [(-1, 0), (0, 1)], [(-1, 0), (0, -1)]]
four = [[(1, 0), (0, 1), (0, -1)], [(-1, 0), (0, 1), (0, -1)], [(0, 1), (1, 0), (-1, 0)], [(0, -1), (1, 0), (-1, 0)]]
five = [[(1, 0), (0, 1), (0, -1), (-1, 0)]]
cctv = {1: one, 2: two, 3: three, 4: four, 5: five}

def do(s, m, temp_map):
    q = deque()
    q.append(s)
    while q:
        p = q.popleft()
        if 0 <= p[0]+m[0] < xM and 0 <= p[1]+m[1] < yM:
            if temp_map[p[0]+m[0]][p[1]+m[1]] in [0, -1]:
                temp_map[p[0]+m[0]][p[1]+m[1]] = -1
                q.append( (p[0]+m[0], p[1]+m[1]) )
            elif temp_map[p[0]+m[0]][p[1]+m[1]] != 6:
                q.append( (p[0]+m[0], p[1]+m[1]) )
    return temp_map

# 모든 경우의 수 다 해보기.
# MAX 65,536
def watch(length, temp_map):
    global result
    if length == len(cctv_list):
        result = min(result, blind_spot(temp_map))
        return 0;
    for ms in cctv[cctv_list[length][0]]:
        copy_map = copy.deepcopy(temp_map)
        for m in ms:
            copy_map = do(cctv_list[length][1], m, copy_map)
        watch(length+1, copy_map)
        # print('--------------------',cctv_list[length][0],'개')
        # for row in copy_map:
        #     print(row)

    
watch(0, _map)
print(result)