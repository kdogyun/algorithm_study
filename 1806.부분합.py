import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(input().split())

start, end, count = 0, 0, float('inf')
num = int(nums[end])
temp = 1

while start <= len(nums) -1:
    while end+1 < len(nums):
        if num >= s :
            break
        end += 1
        num += int(nums[end])
        temp += 1

    if num >= s and temp < count:
        count = temp
    
    num -= int(nums[start])
    temp -= 1
    start += 1

if count == float('inf'):
    count = 0
print(count)