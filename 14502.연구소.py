import sys
input = sys.stdin.readline
import copy

def count_safe_room(array):
    safe_room = 0
    for i in array:
        for x in i:
            if x == '0':
                safe_room += 1
    return safe_room

def go_virus(array):
    queue = []
    for idx_row, i in enumerate(array):
        for idx_hor, x in enumerate(i):
            if x == '2':
                queue.append((idx_row, idx_hor))

    temp = copy.deepcopy(array)

    while len(queue) != 0:
        point = queue.pop(0)
        
        # 상 (-1, 0)
        if point[0] - 1 >= 0 and temp[point[0] - 1][point[1]] == '0':
            temp[point[0] - 1][point[1]] = '2'
            queue.append((point[0] - 1, point[1]))
        # 하 (1, 0)
        if point[0] + 1 < len(array) and temp[point[0] + 1][point[1]] == '0':
            temp[point[0] + 1][point[1]] = '2'
            queue.append((point[0] + 1, point[1]))
        # 좌 (0, -1)
        if point[1] - 1 >= 0 and temp[point[0]][point[1] - 1] == '0':
            temp[point[0]][point[1] - 1] = '2'
            queue.append((point[0], point[1] - 1))
        # 우 (0, 1)
        if point[1] + 1 < len(array[point[0]]) and temp[point[0]][point[1] + 1] == '0':
            temp[point[0]][point[1] + 1] = '2'
            queue.append((point[0], point[1] + 1))

    return count_safe_room(temp)

def build_wall(array):
    queue = []
    for idx_row, i in enumerate(array):
        for idx_hor, x in enumerate(i):
            if x == '0':
                queue.append((idx_row, idx_hor))

    result = []

    for i in range(len(queue) - 2):
        for j in range(i+1, len(queue) - 1):
            for z in range(j+1, len(queue)):
                temp = copy.deepcopy(array)
                temp[queue[i][0]][queue[i][1]] = '1'
                temp[queue[j][0]][queue[j][1]] = '1'
                temp[queue[z][0]][queue[z][1]] = '1'
                result.append(go_virus(temp))

    print(max(result))


n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(input().split()))
build_wall(array)