import sys
sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

class max_heap():
    def __init__(self):
        self.array = [None]

    def insert(self, num):
        self.array.append(num)
        pos = len(self.array) - 1

        if pos > 1:
            while int(pos/2) > 0 and self.array[pos] > self.array[int(pos/2)] :
                temp = self.array[pos]
                self.array[pos] = self.array[int(pos/2)]
                self.array[int(pos/2)] = temp
                pos = int(pos/2)

    def pop(self):
        return self.array.pop(1)

n, m, k = map(int, input().rstrip().split())
heap_list = {str(i):max_heap() for i in range(1, n+1)}

for _ in range(m):
    scores = list(input().rstrip().split())
    for i in range(n):
        heap_list[scores[i*2]].insert(float(scores[i*2+1]))

max_list = []
for key in heap_list:
    max_list.append(heap_list[key].pop())

max_list.sort(reverse=True)
sum = 0
for i in range(k):
    sum += max_list[i]
print(round(sum,1))