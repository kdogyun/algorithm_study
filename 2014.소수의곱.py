import sys
sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

class min_heap():
    def __init__(self):
        self.array = [None]

    def insert(self, num):
        self.array.append(num)
        pos = len(self.array) - 1

        if pos > 1:
            while int(pos/2) > 0 and self.array[ int(pos/2) ] > num:
                temp = self.array[ int(pos/2) ]
                self.array[ int(pos/2) ] = num
                self.array[ pos ] = temp
                pos = int(pos/2)

    def delete(self):
        first = 0

        if len(self.array) > 1:
            last = self.array.pop()
            first = last

            if len(self.array) > 1:
                first = self.array[1]
                self.array[1] = last
                
                pos = 1
                while pos*2 < len(self.array):
                    if pos*2+1 >= len(self.array):
                        next_pos = pos*2
                    elif self.array[ pos*2 ] < self.array[ pos*2 + 1]:
                        next_pos = pos*2
                    else:
                        next_pos = pos*2 +1

                    if self.array[ next_pos ] < last:
                        temp = self.array[ next_pos ]
                        self.array[ next_pos ] = last
                        self.array[ pos ] = temp
                        pos = next_pos
                    else:
                        break

        return first
        
heap = min_heap()
k, n = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
used = set([])
for x in nums:
    heap.insert(x)
    used.add(x)

result = 0
for i in range(n):
    result = heap.delete()
    for x in nums:
        if x*result not in used:
            heap.insert(x*result)
            used.add(x*result)
print(result)