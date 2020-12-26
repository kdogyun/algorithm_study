import sys
input = sys.stdin.readline

m, n = map(int, input().split())
array = []
for _ in range(m):
    array.append(list(input()))

def go(array):
    move = [(0,1), (0,-1), (1,0), (-1,0)]
    visited = array.copy()
    queue = []
    for i in range(len(array[0])-1):
        if array[0][i] == '0':
            queue.append( (0, i) )
    result = False
    while queue:
        point = queue.pop(0)
        if point[0] == len(array) - 1:
            result = True
            break
        visited[point[0]][point[1]] = '1'
        for m in move:
            if 0 <= point[0] + m[0] < len(array) and 0<= point[1] + m[1] < len(array[0])-1 and array[point[0] + m[0]][point[1] + m[1]] =='0' and visited[point[0] + m[0]][point[1] + m[1]] =='0':
                queue.insert(0, (point[0] + m[0], point[1] + m[1]))
    return result

if go(array):
    print('YES')
else:
    print('NO')