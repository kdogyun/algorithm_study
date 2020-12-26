import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))
s = sum(nums)

length = int(s/m)

max_len = 0
for l in range(round(length,-(len(str(length))-1)), length+1):
    count = 0
    for i in nums:
        count += int(i/l)
    if count >= m and max_len < l:
        max_len = l

print(max_len)