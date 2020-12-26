n = int(input())
num_list = [0] * 1000001

def make_one(num):
    for i in range(1, num+1):
        if i == 1 :
            num_list[i] = 0
            continue
        num_list[i] = num_list[i-1] + 1
        if i % 2 == 0:
            num_list[i] = min(num_list[i], num_list[i//2] + 1)
        if i % 3 == 0:
            num_list[i] = min(num_list[i], num_list[i//3] + 1)
    return num_list[num]

print(make_one(n))

'''
Bottom2Top
1번 규칙 (3으로 나누어 떨어진다) : D[N] = D[N/3] + 1
2번 규칙 (2로 나누어 떨어진다) : D[N] = D[N/2] + 1
3번 규칙 ( 1 을 뺀다 ): D[N] = D[N-1] + 1
'''

# 이런 점화식을 세우는 것이 DP의 핵심!
