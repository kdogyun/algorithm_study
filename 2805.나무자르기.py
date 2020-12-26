import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = []

for i in list(input().rstrip().split()):
    trees.append(int(i))

