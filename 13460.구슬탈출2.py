import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()
import copy

n, mm = map(int, input().split())
_map = [ ]
red = []
blue = []
goal = []

for x in range(n):
    temp = list(input())
    for y in range(mm):
        if temp[y] == 'R':
            red = [x, y]
        if temp[y] == 'B':
            blue = [x, y]
        if temp[y] == 'O':
            goal = [x, y]
    _map.append(temp)

move = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 위 아래 좌 우
result = 11

def simulation(count, map_temp, red_pos, blue_pos, goal_pos):
    global result
    if count > 1:
        pass
    elif blue_pos == goal_pos:
        pass
    elif red_pos == goal_pos:
        print(count)
        result = min(result, count)
    else:
        for m in move:
            tmap = copy.deepcopy(map_temp)

            x = y = 0
            if 0 <= red_pos[0] + m[0] * (x+1) < n and 0 <= red_pos[1] + m[1] * (x+1) < mm:
                while map_temp[red_pos[0] + m[0] * (x+1)][red_pos[1] + m[1] * (x+1)] == '.':
                    x += 1
                    if n-1 <= red_pos[0] + m[0] * (x+1) or 0 >= red_pos[0] + m[0] * (x+1):
                        x -= 1
                        break
                    if mm-1 <= red_pos[1] + m[1] * (x+1) or 0 >= red_pos[1] + m[1] * (x+1):
                        x -= 1
                        break
                    if map_temp[red_pos[0] + m[0] * (x+1)][red_pos[1] + m[1] * (x+1)] == 'O':
                        break
                    # print(red_pos[0] + m[0] * (x+1), red_pos[1] + m[1] * (x+1))
                map_temp[red_pos[0] + m[0] * (x+1)][red_pos[1] + m[1] * (x+1)] = '.'
                map_temp[red_pos[0]][red_pos[1]] = 'R'

            if 0 <= blue_pos[0] + m[0] * (y+1) < n and 0 <= blue_pos[1] + m[1] * (y+1) < mm:
                while map_temp[blue_pos[0] + m[0] * (y+1)][blue_pos[1] + m[1] * (y+1)] == '.':
                    y += 1
                    if n-1 <= blue_pos[0] + m[0] * (y+1) or 0 >= blue_pos[0] + m[0] * (y+1):
                        y -= 1
                        break
                    if mm-1 <= blue_pos[1] + m[1] * (y+1) or 0 >= blue_pos[1] + m[1] * (y+1):
                        y -= 1
                        break
                    if map_temp[blue_pos[0] + m[0] * (y+1)][blue_pos[1] + m[1] * (y+1)] == 'O':
                        break

            x1 = copy.deepcopy(x)
            y1 = copy.deepcopy(y)
                
            map_temp = copy.deepcopy(tmap)
            x = y = 0
            if 0 <= blue_pos[0] + m[0] * (y+1) < n and 0 <= blue_pos[1] + m[1] * (y+1) < mm:
                while map_temp[blue_pos[0] + m[0] * (y+1)][blue_pos[1] + m[1] * (y+1)] == '.':
                    y += 1
                    if n-1 <= blue_pos[0] + m[0] * (y+1) or 0 >= blue_pos[0] + m[0] * (y+1):
                        y -= 1
                        break
                    if mm-1 <= blue_pos[1] + m[1] * (y+1) or 0 >= blue_pos[1] + m[1] * (y+1):
                        y -= 1
                        break
                    if map_temp[blue_pos[0] + m[0] * (y+1)][blue_pos[1] + m[1] * (y+1)] == 'O':
                        break
                map_temp[blue_pos[0] + m[0] * (y+1)][blue_pos[1] + m[1] * (y+1)] = '.'
                map_temp[blue_pos[0]][blue_pos[1]] = 'B'

            if 0 <= red_pos[0] + m[0] * (x+1) < n and 0 <= red_pos[1] + m[1] * (x+1) < mm:
                while map_temp[red_pos[0] + m[0] * (x+1)][red_pos[1] + m[1] * (x+1)] == '.':
                    x += 1
                    if n-1 <= red_pos[0] + m[0] * (x+1) or 0 >= red_pos[0] + m[0] * (x+1):
                        x -= 1
                        break
                    if mm-1 <= red_pos[1] + m[1] * (x+1) or 0 >= red_pos[1] + m[1] * (x+1):
                        x -= 1
                        break
                    if map_temp[red_pos[0] + m[0] * (x+1)][red_pos[1] + m[1] * (x+1)] == 'O':
                        break
                    # print(red_pos[0] + m[0] * (x+1), red_pos[1] + m[1] * (x+1))

            # print(x1, y1, x, y)
            if x1+y1 > x+y:
                x = x1
                y = y1

            map_temp = copy.deepcopy(tmap)
            if x !=0:
                red_pos = [red_pos[0] + m[0] * (x+1), red_pos[1] + m[1] * (x+1)]
                map_temp[red_pos[0] - m[0] * (x+1)][red_pos[1] - m[1] * (x+1)] = '.'
                map_temp[red_pos[0]][red_pos[1]] = 'R'

            if y != 0:
                blue_pos = [blue_pos[0] + m[0] * (y+1), blue_pos[1] + m[1] * (y+1)]
                map_temp[blue_pos[0] - m[0] * (y+1)][blue_pos[1] - m[1] * (y+1)] = '.'
                map_temp[blue_pos[0]][blue_pos[1]] = 'B'
                
            if x != 0 or y != 0:
                simulation(count+1, map_temp, red_pos, blue_pos, goal_pos)

                map_temp[red_pos[0] - m[0] * (x+1)][red_pos[1] - m[1] * (x+1)] = 'R'
                map_temp[red_pos[0]][red_pos[1]] = '.'
                map_temp[blue_pos[0] - m[0] * (y+1)][blue_pos[1] - m[1] * (y+1)] = 'B'
                map_temp[blue_pos[0]][blue_pos[1]] = '.'

                red_pos = [red_pos[0] - m[0] * (x+1), red_pos[1] - m[1] * (x+1)]
                blue_pos = [blue_pos[0] - m[0] * (y+1), blue_pos[1] - m[1] * (y+1)]
                
simulation(0, _map, red, blue, goal)

if result == 11:
    print(-1)
else:
    print(result)