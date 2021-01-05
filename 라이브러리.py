from collections import deque
deq = deque()
deq.append(1) # 오른쪽에 삽입
deq.appendleft(2) # 왼쪽에 삽입
deq.popleft() # 왼쪽 꺼내기
deq.pop() # 오른쪽 꺼내기
print(deq)

