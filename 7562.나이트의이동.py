import sys
input = sys.stdin.readline

move = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, -2), (-1, -2), (1, 2), (-1, 2)]

for _ in range(int(input())):
    l = int(input())
    array = [[float('inf') for i in range(l)] for i in range(l)]

    a, b = map(int, input().split())
    curr = (a, b)
    a, b = map(int, input().split())
    target = (a, b)

    if curr == target:
        print(0)
        continue

    queue = [(curr, 0)]
    cost = float('inf')

    while True:
        point = queue.pop(0)
        if point[0] == target:
            cost = point[1]
            break

        for i in move:
            next_x = point[0][0] + i[0]
            next_y = point[0][1] + i[1]
            next_cost = point[1] + 1

            if next_x >= 0 and next_x < l and next_y >=0 and next_y < l and next_cost < array[next_x][next_y]:
                array[next_x][next_y] = next_cost
                queue.append(((next_x, next_y), next_cost))
    print(cost)

