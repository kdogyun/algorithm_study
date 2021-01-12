import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def dfs(arr, depth, n, k, idx):
    global lo
    # arr 원 배열, depth 진행깊이, n 원 배열의 길이, k 뽑을 갯수, idx 진행할 인덱스 넘버
    if depth == k:
        print(' '.join(map(str, lotto)))
        return
    
    for i in range(idx, n):
        lotto.append(arr[i])
        dfs(arr, depth+1, n, k, i+1)
        lotto.pop()

while True: 
    lotto = []
    lo = []
    nums = deque(map(int, input().split()))
    n = nums.popleft()
    if not n: break;
    dfs(nums, 0, n, 6, 0)
    print()