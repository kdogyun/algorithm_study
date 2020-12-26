import sys
input = sys.stdin.readline

def result(arrayA, arrayB):
    a = 0
    for i in range(len(arrayA)):
        a += int(arrayA[i]) * int(arrayB[i])
    return a

def cal(nums, pre):
    global array

    last = (len(nums) == 1)

    for i in range(len(nums)):
        item = list(pre + nums[i])
        if last:
            array.append(result(item, arrayB))
        else:
            
            cal()


n = int(input())
arrayA = list(input().split())
arrayB = list(input().split())

