import sys
input = sys.stdin.readline
import copy

def find_path_cost(map, start, end):
    temp = [[float('inf') for i in range(len(map[0]))] for i in range(len(map))]
    queue = []
    queue.append((start[0], start[1], 0))

    while len(queue) != 0:
        point = queue.pop(0)

        if map[point[0]][point[1]] == '1':
            continue
        
        # 상 (-1, 0)
        if point[0] - 1 >= 1 and temp[point[0] - 1][point[1]] > point[2] and map[point[0] - 1][point[1]] != '1':
            temp[point[0] - 1][point[1]] = point[2]
            queue.append((point[0] - 1, point[1], point[2]+1))
        # 하 (1, 0)
        if point[0] + 1 < len(map) and temp[point[0] + 1][point[1]] > point[2] and map[point[0] + 1][point[1]] != 1:
            temp[point[0] + 1][point[1]] = point[2]
            queue.append((point[0] + 1, point[1], point[2]+1))
        # 좌 (0, -1)
        if point[1] - 1 >= 1 and temp[point[0]][point[1] - 1] > point[2] and map[point[0]][point[1] - 1] != '1':
            temp[point[0]][point[1] - 1] = point[2]
            queue.append((point[0], point[1] - 1, point[2]+1))
        # 우 (0, 1)
        if point[1] + 1 < len(map[point[0]]) and temp[point[0]][point[1] + 1] > point[2] and temp[point[0]][point[1] + 1] != '1':
            temp[point[0]][point[1] + 1] = point[2]
            queue.append((point[0], point[1] + 1, point[2]+1))
    return temp[end[0]][end[1]]

def find_customer(customers, map, start):
    customer_list = []
    customers_copy = copy.deepcopy(customers)
    while len(customers_copy) != 0:
        custom = customers_copy.pop(0)
        cost = find_path_cost(map, start, (custom[0], custom[1]))
        customer_list.append((custom[0], custom[1], custom[2], custom[3],  cost))
    customer_list = sorted(customer_list, key = lambda x : (x[4], x[0], x[1]))
    return customer_list[0]

def drive(customers, map, start, fuel):
    result = fuel
    start = start
    # while fuel > 0 or len(customers) != 0:
    while len(customers) != 0:
        # 태울 손님 찾기
        custom = find_customer(customers, map, start)
        customers.remove((custom[0], custom[1], custom[2], custom[3]))
        
        # 손님 태우러 가는 도중 연료 체크
        if fuel - custom[4] < 0:
            result = -1
            break
        fuel -= custom[4]

        # 손님 태우고 이동하는 도중 연료 체크
        cost = find_path_cost(map, (custom[0], custom[1]), (custom[2], custom[3]))
        if fuel - cost < 0:
            result = -1
            break
        fuel -= cost
        fuel += cost*2
        result = fuel

        # 택시 출발위치 업데이트
        start = (custom[2], custom[3])
    print(result)
    



n, m, f = map(int, input().split()) # n=맵 크기, m=목표 손님, f=연료
array = []
array.append(['0' for i in range(n+1)])
for _ in range(n):
    a = list(input().split())
    a.insert(0,'0')
    array.append(a)
x, y = map(int, input().split())
start = (x,y)
customers = []
for _ in range(m):
    x, y, dx, dy = map(int, input().split())
    customers.append((x, y, dx, dy))
drive(customers, array, start, f)