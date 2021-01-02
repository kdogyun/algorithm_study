import sys
sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
beers = []
for i in range(k):
    beers.append(tuple(map(int, input().rstrip().split())))
beers = sorted(beers, key= lambda x: (x[0], -x[1]))

gate = True
limit = 0
remove = []
for idx, (favor, alcohol) in enumerate(beers):
    limit += favor

    out = idx + n
    temp_favor = 0
    if out >= len(beers): out = len(beers);
    for i in range(idx, out):
        temp_favor += beers[i][0]
    if temp_favor >= m:
        gate = False
        break
    remove.append(idx)

if limit < m and gate:
    print(-1)
else:
    remove.sort(reverse=True)
    for i in remove:
        beers.pop(i)

    beers = sorted(beers, key= lambda x: x[1])
    print(beers[0][1])