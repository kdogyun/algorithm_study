import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()

str1 = list(input())
str2 = list(input())
dp = [[0 for i in range(len(str1)+1)] for i in range(len(str2)+1)]

for x, s2 in enumerate(str2):
    for y, s1 in enumerate(str1):
        if s1 == s2:
            dp[x+1][y+1] = dp[x][y] + 1
        else:
            dp[x+1][y+1] = max(dp[x][y+1], dp[x+1][y])
            
print(dp[len(str2)][len(str1)])