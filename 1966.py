import sys
input = sys.stdin.readline

class queue():
    def __init__(self):
        self.array = []
        self.tail = -1
    
    def push(self, x):
        self.array.append(x)
        self.tail += 1
    
    def pop(self):
        if self.tail > -1:
            num = self.array.pop(0)
            self.tail -= 1
            return num
        return -1
    
    def empty(self):
        if self.tail == -1:
            return 1
        return 0

class printer():
    def __init__(self, num, w):
        self.printer_num = num
        self.weight = w
            
q = queue()

for _ in range(int(input())): # test-case 수
    n, m = map(int, input().split())
    w = list(input().split())
    result = []

    for i in range(n):
        q.push(printer(i, w[i]))
    
    while not q.empty():
        first_q = q.pop()
        comp = True
        for comp_q in q.array:
            if first_q.weight < comp_q.weight:
                comp = False
                break
        if not comp :
            q.push(first_q)
        else:
            result.append(first_q)
    
    for i in range(len(result)):
        if result[i].printer_num == m:
            print(i+1)
            break