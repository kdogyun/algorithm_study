n, m, k = map(int, input().split())
num_list = []

for i in range(n):
    num_list.append(int(input()))

for i in range(m+k):
    a, b, c = map(int, input().split())
    if a==1:
        num_list[b-1] = c
    elif a==2:
        print('b~c sum')

def dvide_conquer(q, start, end):
     