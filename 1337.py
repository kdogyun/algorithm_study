n = int(input())

num_list = []
for i in range(n):
    num = int(input())
    num_list.append(num)
num_list.sort()

diff_list = []
for i in range(n):
    if i == 0:
        diff = 0
    else:
        diff = num_list[i] - num_list[i-1]
    diff_list.append(diff)

min = n
for i in range(n-1):
    acc = 0
    count = 1
    for j in range(i+1, n):
        count += 1
        acc += diff_list[j]
        if acc > 4:
            break
        else:
            if min > 5 - count:
                min = 5 - count
            
print(min)