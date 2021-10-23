import sys
sys.stdin = open("test.txt", "r")

answer = 0
n = int(input())

pos = [(0, -1), (1, 0), (0, 1), (-1, 0)]
a = [list(map(int, input().split())) for _ in range(n)]

t = [(n//2, n//2)]

# 11 22 33 44 55 66 7
# 총 횟수... n*2 - 1

for i in range(2*n - 1):
    for j in range(int(i/2)+1):
        for x, y in t:
            sx = x + pos[i%4][0]
            sy = y + pos[i%4][1]
            t = [(sx, sy)]

            send = a[sx][sy]
            a[sx][sy] = 0

            p1 = int(send * 0.01)
            p2 = int(send * 0.02)
            p5 = int(send * 0.05)
            p7 = int(send * 0.07)
            p10 = int(send * 0.1)
            send -= (p1*2 + p2*2 + p5 + p7*2 + p10*2)

            if 0<= sx + pos[i%4][0] <n and 0<= sy + pos[i%4][1] <n:
                a[sx + pos[i%4][0]][sy + pos[i%4][1]] += send
            else:
                answer += send
            if 0<= sx + pos[i%4][0]*2 <n and 0<= sy + pos[i%4][1]*2 <n:
                a[sx + pos[i%4][0]*2][sy + pos[i%4][1]*2] += p5
            else:
                answer += p5
            if 0<= sx + pos[(i+3)%4][0] <n and 0<= sy + pos[(i+3)%4][1] <n:
                a[sx + pos[(i+3)%4][0]][sy + pos[(i+3)%4][1]] += p7
            else:
                answer += p7
            if 0<= sx + pos[(i+3)%4][0]*2 <n and 0<= sy + pos[(i+3)%4][1]*2 <n:
                a[sx + pos[(i+3)%4][0]*2][sy + pos[(i+3)%4][1]*2] += p2
            else:
                answer += p2
            if 0<= sx + pos[(i+1)%4][0] <n and 0<= sy + pos[(i+1)%4][1] <n:
                a[sx + pos[(i+1)%4][0]][sy + pos[(i+1)%4][1]] += p7
            else:
                answer += p7
            if 0<= sx + pos[(i+1)%4][0]*2 <n and 0<= sy + pos[(i+1)%4][1]*2 <n:
                a[sx + pos[(i+1)%4][0]*2][sy + pos[(i+1)%4][1]*2] += p2
            else:
                answer += p2
            if 0<= sx + pos[i%4][0] + pos[(i+1)%4][0] <n and 0<= sy + pos[i%4][1] + pos[(i+1)%4][1] <n:
                a[sx + pos[i%4][0] + pos[(i+1)%4][0]][sy + pos[i%4][1] + pos[(i+1)%4][1]] += p10
            else:
                answer += p10
            if 0<= sx + pos[i%4][0] + pos[(i+3)%4][0] <n and 0<= sy + pos[i%4][1] + pos[(i+3)%4][1] <n:
                a[sx + pos[i%4][0] + pos[(i+3)%4][0]][sy + pos[i%4][1] + pos[(i+3)%4][1]] += p10
            else:
                answer += p10
            if 0<= sx + pos[(i+2)%4][0] + pos[(i+1)%4][0] <n and 0<= sy + pos[(i+2)%4][1] + pos[(i+1)%4][1] <n:
                a[sx + pos[(i+2)%4][0] + pos[(i+1)%4][0]][sy + pos[(i+2)%4][1] + pos[(i+1)%4][1]] += p1
            else:
                answer += p1
            if 0<= sx + pos[(i+2)%4][0] + pos[(i+3)%4][0] <n and 0<= sy + pos[(i+2)%4][1] + pos[(i+3)%4][1] <n:
                a[sx + pos[(i+2)%4][0] + pos[(i+3)%4][0]][sy + pos[(i+2)%4][1] + pos[(i+3)%4][1]] += p1
            else:
                answer += p1

print(answer)