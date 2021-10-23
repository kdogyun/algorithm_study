def solution(grid):
    answer = 0

    # 오, 왼, 위 , 아
    # 모서리 2개, 나머지 하나씩

    for idx, row in enumerate(grid):
        x = idx
        if x == 0:
            # 왼쪽, 오른쪽
            for direction in ['r', 'l']:
                y = 0
                while x >= 0 and x < len(grid) and y >= 0 and y < len(grid[-1]):
                    if grid[x][y] == 'B' and direction == 'r':
                        if x not in [0, len(grid) - 1]:
                        x -= 1
                
        elif x == len(grid) - 1:
            # 첫번째 왼쪽, 아래쪽
            # 마지막 아래쪽, 오른쪽
            # 나머지 아래쪽
            pass
        else:
            # 첫번째 왼쪽
            # 마지막 오른쪽
            pass

    return answer


test = [['B', 'RRB'], ['R', 'BBB', 'RBRBR'], ['R', 'RRR', 'RBBBB', 'BRRRBRR']]
for data in test:
    print( solution(data) )