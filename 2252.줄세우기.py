import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = { i:[] for i in range(n+1)}
topol = [0 for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    topol[b] += 1
queue = []
for i in range(len(topol)):
    if i != 0 and topol[i] == 0:
        queue.append(i)

result = []
while queue:
    point = queue.pop(0)
    result.append(point)
    if len(result) == n:
        break
    # for i in graph[point]:
    #     topol[i] -= 1
    #     if topol[i] == 0
    # for i in range(len(topol)):
    #     if i != 0 and topol[i] == 0 and i not in result+queue:
    #         queue.append(i)
    for i in graph[point]:
        topol[i] -= 1
        if topol[i] == 0 and i not in result+queue:
            queue.append(i)

for i in result:
    print(i, end=' ')