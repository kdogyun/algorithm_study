import sys
sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

# 슬라임 합치기 처럼 최소힙을 구현하기 귀찮아서
# list와 sort로 반복돌렸는데.... 시간 초과뜸..
# 엄청나게 많은 숫자면 (혹은 반복횟수면)
# 힙이 시간이 더 적게 걸림.

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

cards = min_heap()
for _ in range(int(input())):
    cards.insert(int(input()))

result = 0
while len(cards.array) != 2:
    a = cards.delete()
    b = cards.delete()

    cards.insert(a+b)
    result += a + b

print(result)