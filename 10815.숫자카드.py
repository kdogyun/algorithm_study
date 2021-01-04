import sys
input = sys.stdin.readline

class binary():
    def __init__(self):
        self.array = []
    
    def search(self, start, end, num): # O(logn)
        mid = int((start+end) / 2)
        if start > len(self.array) or end < 0 or start > end:
            return False, start
        
        if self.array[mid] == num:
            return True, mid
        elif start == end:
            if self.array[mid] > num:
                return False, start
            else:
                return False, start + 1
        elif self.array[mid] > num:
            return self.search(start, mid-1, num)
        else:
            return self.search(mid+1, end, num)

    def insert(self, num):
        _, pos = self.search(0, len(self.array) - 1, num)
        self.array.insert(pos, num)

n = int(input())
bina = binary()
a = list(input().rstrip().split())
a.sort(reverse=True)
for i in a:
    bina.insert(int(i))

m = int(input())
for i in list(input().rstrip().split()):
    re, _ = bina.search(0, n-1, int(i))
    if re:
        print(1, end=' ')
    else:
        print(0, end=' ')