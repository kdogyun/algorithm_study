import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
house = []
for _ in range(n):
    house.append(list(map(int, input().split())))

check = {0: [(0, 1)], 1:[(1, 0)], 2:[(0, 1), (1, 0), (1, 1)]}
go = {0: [0, 2], 1: [1, 2], 2: [0, 1, 2]}

