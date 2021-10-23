
def solution(money, cost):
    answer = 0
    
    interval_sum = 0
    end = 0
    length = len(cost)

    for start in range(length):
        while interval_sum < money and end < length:
            interval_sum += cost[end]
            end += 1
        if interval_sum <= money:
            answer = max(answer, end - start + 1)
        interval_sum -= cost[start]
    return answer

test = [(420, [0, 900, 0, 200, 150, 0, 30, 50]), (100, [245, 317, 151, 192])]
for data in test:
    print( solution( *data ) )