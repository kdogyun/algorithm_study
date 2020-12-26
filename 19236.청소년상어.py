import sys
input = sys.stdin.readline

move = [ (0,0), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1) ]
fish = {i : [0,0] for i in range(16+1)}
array = [[] for i in range(4)]

for i in range(4):
    fishs = list(input().split())
    for x in range(4):
        array[i].append( [int(fishs[2*x]), int(fishs[2*x+1])] )
        fish[int(fishs[2*x])] = [i, x]
results = []
def go(arr, fishs, count):
    if len(fishs) == 1:
        results.append(count)
        return
    for key in fishs: #남아있는 물고기 번호 순대로 움직이기
        if key:
            point = fishs[key]
            moving_origin = arr[point[0]][point[1]][1]
            moving = moving_origin
            for turn in range(8): #물고기 회전
                moving = (moving_origin - 1 + turn) % 8 + 1
                if 0<= point[0]+move[moving][0] <=3 and 0<= point[1]+move[moving][1] <=3: #경계 안 인지 확인
                    if arr[point[0]+move[moving][0]][point[1]+move[moving][1]][0] != 0: #상어가 아니면
                        if arr[point[0]+move[moving][0]][point[1]+move[moving][1]][0] == None: #빈 자리면
                            arr[point[0]+move[moving][0]][point[1]+move[moving][1]] = arr[point[0]][point[1]]
                            arr[point[0]][point[1]] = [None, None]
                            fishs[key] = [point[0]+move[moving][0], point[1]+move[moving][1]]
                            break
                        else: #다른 물고기가 있을 경우
                            temp = arr[point[0]+move[moving][0]][point[1]+move[moving][1]]
                            arr[point[0]+move[moving][0]][point[1]+move[moving][1]] = arr[point[0]][point[1]]
                            arr[point[0]][point[1]] = temp
                            fishs[key] = [point[0]+move[moving][0], point[1]+move[moving][1]]
                            fishs[temp[0]] = [point[0], point[1]]
                            break
    for i in range(1,4):
        point = fishs[0]
        moving_origin = arr[point[0]][point[1]][1]
        moving = moving_origin
        if moving is None:
            continue
        cnt = 0
        for turn in range(8): #상어 회전
            cnt += 1
            moving = (moving_origin - 1 + turn) % 8 + 1
            if 0<= point[0]+move[moving][0]*i <=3 and 0<= point[1]+move[moving][1]*i <=3 and arr[point[0]+move[moving][0]*i][point[1]+move[moving][1]*i][0] is not None: #경계 안 인지, 물고기가 없는 곳인지 확인
                if 1 <= arr[point[0]+move[moving][0]*i][point[1]+move[moving][1]*i][0] <= 16: #물고기 이면
                    temp_fishs = fishs.copy()
                    temp_arr = arr.copy()
                    temp_count = count
                    temp_count += arr[point[0]+move[moving][0]*i][point[1]+move[moving][1]*i][0]
                    del temp_fishs[arr[point[0]+move[moving][0]*i][point[1]+move[moving][1]*i][0]]
                    temp_fishs[0] = [point[0]+move[moving][0]*i, point[1]+move[moving][1]*i]
                    temp_arr[point[0]+move[moving][0]*i][point[1]+move[moving][1]*i] = [0, temp_arr[point[0]+move[moving][0]*i][point[1]+move[moving][1]*i][1]]
                    temp_arr[point[0]][point[1]] = [None, None]
                    go(temp_arr, temp_fishs, temp_count)
                    cnt -= 1
                    break # 물고기를 만나서 먹어치우고 자리 바꾸기
        if cnt == 8: #먹을수 있는 물고기가 없을 때
            results.append(count)




temp = array[0][0]
array[0][0] = [0, temp[1]]
del fish[temp[0]]

for idx in range(len(array)):
    print(array[idx])
go(array, fish, temp[0])
print(max(results))