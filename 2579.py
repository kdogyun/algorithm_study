n = int(input())

scores = []
for i in range(n):
    scores.append(int(input()))

dp = [ 0 * i for i in range(n)]
if n >= 1:
    dp[0] = scores[0]
if n >= 2:
    dp[1] = max(scores[0] + scores[1], scores[1])
if n >= 3:
    dp[2] = max(scores[1]+scores[2], scores[0]+scores[2])
if n >= 4:
    for i in range(3, n):
        dp[i] = max(scores[i] + dp[i-2], scores[i] + scores[i-1] + dp[i-3])

print(dp[n-1])

'''
dp[n] = dp[n-2] + arr[n]                // 마지막계단과 전전계단까지의 최댓값
dp[n] = dp[n-3] + arr[n-1] + arr[n]     // 마지막계단과 전계단, 전전전계단까지의 최댓값
2칸을 뛰우면 앞에 뭐가 오든 상관없으니 2칸을 뛰울때 까지로 수열을 만드는 것
'''

# 이런 점화식을 세우는 것이 DP의 핵심!