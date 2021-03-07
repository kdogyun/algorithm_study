import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n = int(input())
_map = [ [ 0 for i in range(n) ] for i in range(n) ]
_map[0][0] = -1

for _ in range(int(input())):
    x, y = map(int, input().split())
    _map[x-1][y-1] = 1

comm = {}
for _ in range(int(input())):
    t, d = input().split()
    comm[int(t)] = 1 if d == 'D' else -1

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
m = 0
time = 0
q = deque()
q.append((0, 0))
while True:
    time += 1
    tail = q[0]
    head = q[-1]
    next_pos = (head[0] + move[m][0], head[1] + move[m][1])
    
    if 0 <= next_pos[0] < n and 0 <= next_pos[1] < n:
        if _map[next_pos[0]][next_pos[1]] == -1: break;
        if _map[next_pos[0]][next_pos[1]] == 0:
            q.popleft()
            _map[tail[0]][tail[1]] = 0
        _map[next_pos[0]][next_pos[1]] = -1
        q.append(next_pos)

    else: break;

    if comm.setdefault(time, 0):
        m = (m+comm[time])%4
    print('----------------------', time, '초')
    for row in _map:
        for item in row:
            print(item, end=' ')
        print()

print(time)