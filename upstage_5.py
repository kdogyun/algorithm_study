# 5
import heapq

class ProblemPy:
    @staticmethod
    def solve(n, e, companies, subway_map):
        # IMPLEMENT HERE
        transfer = 0
        dist = 0
        # graph: time
        graph = {i:{} for i in range(n)}
        for i in range(n):
            for j in range(n):
                if subway_map[i][j] == 0:
                    continue
                graph[i][j] = subway_map[i][j]
        print(graph)
        transfer, dist = find(graph, e, companies)
        return transfer, dist


def find(graph, end, companies):
    # v : [transfer, time, start]
    distances = {v: [float('inf'), float('inf'), 0] for v in graph}

    distances[0] = [0, 0, 0]
    queue = []

    heapq.heappush(queue, [distances[0][0], distances[0][1], 0])

    while queue:
        cur_trans, cur_dis, cur_ver = heapq.heappop(queue)

        if distances[cur_ver][0] < cur_trans:
            continue

        if distances[cur_ver][1] < cur_dis:
            continue

        for next, cost in graph[cur_ver].items():
            dis = cur_dis + cost
            trans = cur_trans + 1 if companies[cur_ver] != companies[next] else 0

            if dis < distances[next][0] and trans <= distances[next][1]:
                distances[next] = [trans, dis, cur_ver]
                heapq.heappush(queue, [trans, dis, next])
        
        print(cur_ver, distances)
    return distances[end][0], distances[end][1]

    
# DO NOT MODIFY FROM HERE
n = 6
e = 3
companies = [0, 1, 1, 1, 1, 1]
subway_map = [[0, 3, 1, 0, 10, 0], [3, 0, 0, 15, 0, 0], [1, 0, 0, 0, 0, 1], [0, 15, 0, 0, 1, 0], [10, 0, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0]]
print(ProblemPy.solve(n, e, companies, subway_map))