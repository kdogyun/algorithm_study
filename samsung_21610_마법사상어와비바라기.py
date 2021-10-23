import sys
sys.stdin = open("test.txt", "r")

pos = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
n, m = map(int, input().split())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

cloud = [[0 for _ in range(n)] for _ in range(n)]
cloud[n-1][0] = 1
cloud[n-1][1] = 1
cloud[n-2][0] = 1
cloud[n-2][1] = 1

for _ in range(m):
    clouds = []
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                clouds.append((i, j))
                cloud[i][j] = 0

    d, s = map(int, input().split())

    waters = []
    for c in clouds:
        x = (n + c[0] + pos[d-1][0] * s) % n
        y = (n + c[1] + pos[d-1][1] * s) % n

        cloud[x][y] += 1
        waters.append((x, y))
        a[x][y] += 1
    # clouds = []

    for w in waters:
        for p in range(len(pos)):
            if p % 2 == 1:
                x = w[0] + pos[p][0]
                y = w[1] + pos[p][1]

                if x >= n or x < 0:
                    continue
                if y >= n or y < 0:
                    continue

                if a[x][y] > 0:
                    a[w[0]][w[1]] += 1

    for i in range(n):
        for j in range(n):
            if a[i][j] >= 2:
                if (i, j) in waters:
                    pass
                else:
                    cloud[i][j] = 1
                    a[i][j] -= 2

    for x, y in waters:
        cloud[x][y] = 0

answer = 0
for row in a:
    answer += sum(row)

print(answer)