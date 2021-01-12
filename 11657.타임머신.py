import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
graph = {i:{} for i in range(n)}

for _ in range(m):
    a, b, c = map(int, input().split())
    if b-1 not in graph[a-1]:
        graph[a-1][b-1] = c
    graph[a-1][b-1] = min(c, graph[a-1][b-1])

def search(graph, n):
    cost  = [float('inf') for i in range(n)]
    cost[0] = 0
    for _ in range(n):
        for start in range(n):
            for end in graph[start]:
                cost[end] = min(cost[end], cost[start] + graph[start][end])

    result = True
    for start in range(n):
        for end in graph[start]:
            if cost[end] > cost[start] + graph[start][end]:
                result = False
                break
        if not result: break;
    return result, cost

result, cost = search(graph, n)
if result:
    for i in range(1, n):
        if cost[i] == float('inf'):
            print(-1)
        else:
            print(cost[i])
else:
    print(-1)