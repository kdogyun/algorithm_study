computers = int(input())
line = int(input())
graph = {i:[] for i in range(1,computers + 1)}
visited = [0] * (computers + 1)

for i in range(1, line+1):
    a, b = map(int, input().split())
    graph[a].append(b)
##    graph[b].append(a)
    
def dfs(v):
    visited[v]=1
    for i in range(len(graph[v])):
        nexts=graph[v][i]
        if visited[nexts]:continue
        dfs(nexts)
dfs(1)
print(len(list(filter(lambda x: x==1, visited)))-1)
