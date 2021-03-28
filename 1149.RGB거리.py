import sys
sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

n = int(input())
houses = [[0 for i in range(3)] for i in range(n)]

for i in range(n):
    r, g, b = map(int, input().split())
    houses[i][0] = r
    houses[i][1] = g
    houses[i][2] = b

cost = [[0 for i in range(3)] for i in range(n)]
for i in range(n):
    if i == 0:
        cost[i][0] = houses[i][0]
        cost[i][1] = houses[i][1]
        cost[i][2] = houses[i][2]
    else:
        cost[i][0] = houses[i][0] + min(cost[i-1][1], cost[i-1][2])
        cost[i][1] = houses[i][1] + min(cost[i-1][0], cost[i-1][2])
        cost[i][2] = houses[i][2] + min(cost[i-1][1], cost[i-1][0])

print(min(cost[n-1]))