import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()

def search(graph, n):
    cost = [float('inf') for i in range(n)]
    cost[0] = 0
    for _ in range(n):
        for start in range(n):
            for des in graph[start]:
                cost[des] = min(cost[des], graph[start][des] + cost[start])
    result = True
    for start in range(n):
        for des in graph[start]:
            if cost[des] > graph[start][des] + cost[start]:
                    result = False
                    break
        if not result:
            break
    return result

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    graph = {i:{} for i in range(n)}

    for _ in range(m):
        s, e, t = map(int, input().split())

        if e-1 not in graph[s-1]:
            graph[s-1][e-1] = t
        graph[s-1][e-1] = min(t, graph[s-1][e-1])

        if s-1 not in graph[e-1]:
            graph[e-1][s-1] = t
        graph[e-1][s-1] = min(t, graph[e-1][s-1])

    for _ in range(w):
        s, e, t = map(int, input().split())
        
        if e-1 not in graph[s-1]:
            graph[s-1][e-1] = -t
        graph[s-1][e-1] = min(-t, graph[s-1][e-1])
        
    if search(graph, n):
        print('NO') # True, 음수 무한루프가 없다.
    else:
        print('YES') # False, 음수 무한루프가 있다.
