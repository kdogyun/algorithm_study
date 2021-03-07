import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()

_map = []

for _ in range(int(input())):
    _map.append(list(map(int, input().split())))

zero = 0
one = 0
mone = 0

def checkNum(size, x, y, item):
    result = True
    for _x in range(x, x+size):
        for _y in range(y, y+size):
            if _map[_x][_y] != item:
                result = False
                break
        if not result:
            break
    return result

def divideNconquer(N, startX, startY):
    global zero, one, mone
    if checkNum(N, startX, startY, 0):
        zero += 1
    elif checkNum(N, startX, startY, 1):
        one += 1
    elif checkNum(N, startX, startY, -1):
        mone += 1
    else:
        for x in range(startX, startX+N, N//3):
            for y in range(startY, startY+N, N//3):
                divideNconquer(N//3, x, y)

divideNconquer(len(_map), 0, 0)
print(mone)
print(zero)
print(one)