graph = {'서울': set(['대전', '울산']),
         '대전': set(['울산', '대구', '광주']),
         '울산': set(['대구', '부산']),
         '대구': set(['광주', '부산']),
         '광주': set(['부산', '여수']),
         '부산': set(['여수']),
         '여수': set([])}


def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited



def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
    return result
