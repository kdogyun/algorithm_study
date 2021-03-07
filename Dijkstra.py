import sys
from queue import PriorityQueue

input = sys.stdin.readline
v, e = map(int, input().split())
start = int(input())

graph = { i : [] for i in range(1, v+1) }

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

visited = [0] * (v+1)
dist = [ float('inf') ] * (v+1)

dist[start] = 0
pq = PriorityQueue()

# 0, 1
pq.put([dist[start], start])

while not pq.empty():
    # 0, 1
    cur_distance, cur_node_number = pq.get()
    if visited[cur_node_number]: continue
    visited[cur_node_number] = 1

    for next_node, next_cost in graph[cur_node_number]:
        if visited[next_node]: continue

        if dist[next_node] > dist[cur_node_number] + next_cost:
            dist[next_node] = dist[cur_node_number] + next_cost
            pq.put([dist[next_node], next_node])


for i in range(1, v+1):
    if dist[i] == float('inf'):
        print('INF')
    else:
        print(dist[i])
