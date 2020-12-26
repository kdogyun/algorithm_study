import sys
input = sys.stdin.readline

n, m = map(int, input().split())
names = {}
for _ in range(n):
    name = input().rstrip()
    names[name] = 0

noname = []
for _ in range(m):
    name = input().rstrip()
    if name in names:
        noname.append(name)
noname.sort()
print(len(noname))
for name in noname:
    print(name)