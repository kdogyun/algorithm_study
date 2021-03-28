import sys
input = sys.stdin.readline

# wi > w : V[i-1, w]
# else : max(vi + V[i-1, w-wi], v[i-1, w])

'''
P[i, w] 란 i개의 보석이 있고 배낭의 무게 한도가 w일 때 최적의 이익을 의미한다. 식을 좀 문장으로 풀어보면 이렇다.
# 가로: 무게 한도, 세로: 보석 번호
 i번째 보석이 배낭의 무게 한도보다 무거우면 넣을 수 없으므로 i번째 보석을 뺀 i-1개의 보석들을 가지고 구한 전 단계의 최적값을 그대로 가져온다
- 그렇지 않은 경우, i번째 보석을 위해 i번째 보석만큼의 무게를 비웠을 때의 최적값에 i번째 보석의 가격을 더한 값 or i-1개의 보석들을 가지고 구한 전 단계의 최적값 중 큰 것을 선택한다
'''

def kanpsack(n, w, array):
    a = [[0 for i in range(w+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(w+1):
            # 가로, 세로 첫 번째 인덱스 초기화
            if i==0 or w==0:
                a[i][j] = 0
            # 현재 무게가 i번째의 무게보다 같거나 적어서 배낭에 넣을 수 있다면
            elif array[i][0] <= j:  
                # i번째의 가치 + i번째의 무게를 뺀 나머지 공간에 넣을 수 있는 가치, 바로 윗 칸 가치
                # 를 비교하여 큰 값을 선택
                a[i][j] = max( array[i][1] + a[i-1][j-array[i][0]], a[i-1][j])
            # 배낭에 들어가지 않는다면 바로 윗 칸 가치를 적용
            # 현재 고른 물건이 배낭에 들어가지 않으므로 그 전 물건이 들어갈 수 있었던 가치가
            # 최대이므로 바로 윗칸과 비교한다.
            else:
                a[i][j] = a[i-1][j]
    # 최종적으로 해당 무게에서 넣을 수 있는 최대 가치가 마지막 원소에 저장되어있다.
    return a[n][w]

n, m = map(int, input().split())

array = []
array.append((0, 0))
for i in range(n):
    w, v = map(int, input().split())
    array.append((w, v))

print(kanpsack(n, m, array))
