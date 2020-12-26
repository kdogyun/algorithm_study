n = int(input())

computers = {i:{} for i in range(n+1)}

m = int(input())

for i in range(1, m+1):
    a, b, c = map(int, input().split())
    computers[a][b] = c
    computers[b][a] = c

cost = 0
visited = [0] * (n+1)

new = [[1,0]]

while sum(visited) != n:
    new = sorted(new, key = lambda x : x[1])
    num = new.pop(0)
    
    if visited[num[0]] != 1:
        visited[num[0]] = 1
        cost += num[1]
        
        for i in list(computers[num[0]].keys()):
            if visited[i] != 1:
                new.append([i, computers[num[0]][i]])

print(cost)
