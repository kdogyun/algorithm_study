import sys
import copy
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

move = [(1,0), (0,1), (1,1)]
miro = []
for _ in range(n):
    a = list(map(int, input().split()))
    a.append(0)
    miro.append(a)
miro.append([0 for i in range(m+1)])
candy = copy.deepcopy(miro)

for i in range(n):
    for j in range(m):
        candy[i+1][j] = max(candy[i][j] + miro[i+1][j], candy[i+1][j])
        candy[i][j+1] = max(candy[i][j] + miro[i][j+1], candy[i][j+1])
        candy[i+1][j+1] = max(candy[i][j] + miro[i+1][j+1], candy[i+1][j+1])

print(candy[n][m])