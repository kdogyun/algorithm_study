import sys
sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

n, b = map(int, input().split())
b = bin(b)[2:]
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

def mul(m1, m2):
    temp_matrix = [[0 for i in range(len(m1))] for i in range(len(m2[0]))]
    for x in range(len(m1)):
        for y in range(len(m2[0])):
            for z in range(len(m1[0])):
                temp_matrix[x][y] += m1[x][z] * m2[z][y]
    
    # 어짜피 1000밑에 부분만 체크하므로 1000 단위 위로는 그냥 버려도 무방함.
    for i in range(n):
        for j in range(n):
            temp_matrix[i][j] %= 1000

    return temp_matrix

result = [[1 if i == j else 0 for i in range(len(matrix))] for j in range(len(matrix))]
for i in range(len(b)):
    if i != 0:
        matrix = mul(matrix, matrix)
    if b[ -i -1 ] == '1':
        result = mul(matrix, result)

for row in result:
    for item in row:
        print(item, end=' ')
    print()