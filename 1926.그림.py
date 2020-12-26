import sys
input = sys.stdin.readline

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def count_draw(array):
    visited = [[0 for i in range(len(array[0]))] for i in range(len(array))]
    draw = 0
    max_area = 0

    queue = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            area = 0
            if array[i][j] == '1' and visited[i][j] == 0:
                queue.append((i, j))
                draw += 1
                area += 1
                
            while len(queue) > 0:
                point = queue.pop(0)
                visited[point[0]][point[1]] = 1

                for m in move:
                    next_x = point[0] + m[0]
                    next_y = point[1] + m[1]
                    if next_x >= 0  and next_y >= 0 and next_x < len(array) and next_y < len(array[next_x]) and array[next_x][next_y] == '1' and visited[next_x][next_y] == 0 and (next_x, next_y) not in queue:
                        queue.append((next_x, next_y))
                        area += 1
            if max_area < area:
                max_area = area
    print(draw)
    print(max_area)
            
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(input().split()))

count_draw(array)