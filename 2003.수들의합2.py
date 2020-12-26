import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(input().split())

start, end = 0, 0
count = 0
num = int(nums[end])

while start <= len(nums) -1 :
    while end+1 < len(nums):
        if num >= m:
            break
        num += int(nums[end+1])
        end += 1

    if num == m:
        count += 1
    
    num -= int(nums[start])
    start += 1


print(count)