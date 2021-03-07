import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()

n, r, c = map(int, input().split())

result = 0

while not n == 0:
    pos = 0
    if r < 2 ** (n-1): pos += 0;
    else:
        pos += 2
        r -= 2 ** (n-1)
    if c < 2**(n-1): pos += 0;
    else:
        pos += 1
        c -= 2 ** (n-1)

    result += (2**(n-1)) * (2**(n-1)) * pos
    n -= 1

print(result)