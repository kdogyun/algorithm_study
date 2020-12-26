n, m = map(int, input().split())
arr = list(map(int,input().split()))
count = 0

arr.insert(0, 0)
for i in range(1, n+1):
    arr[i] += arr[i-1]

# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         if arr[j + i - 1] - arr[j-1] == m:
#             count += 1

start = 0
end = 1

while start != n:
    if arr[end] - arr[start] == m:
        count += 1
        start += 1
    elif arr[end] - arr[start] > m:
        start += 1
    else:
        if end != n:
            end += 1
        else:
            start += 1

print(count)

# 투 포인터...
# 구간 합(길이) 등을 구할 때 자주 쓰이는 알고리즘