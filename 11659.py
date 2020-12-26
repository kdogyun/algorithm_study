#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(input().split())
sum_list = []

acc = 0
for i in range(n):
    acc += int(num_list[i])
    sum_list.append(acc)

answer_list = []

for i in range(m):
    start, end = map(int, input().split())
    a = sum_list[end-1]
    if start - 2 >= 0:
        a -= sum_list[start-2]
    answer_list.append(a)

for i in answer_list: print(i);
