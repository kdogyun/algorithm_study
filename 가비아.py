# ## 1번
# def trailingZeros (n):
#     count = 0
#     p = 1
#     while n > p:
#         p *= 5
#         count += n // p
#     return count

# n = 1000
# print(trailingZeros(n))

# ## 2번
# def lengthOfLongestSubstring(s):
#     answer = set([])

#     while len(s):
#         used = ''
#         for index, char in enumerate(s):
#             if char in used:
#                 break
#             used += char
#             answer.add(used)
#         s = s[1:]
#     return len(answer)

# str = 'zxzx'
# print(lengthOfLongestSubstring(str))

## 3번
# from collections import deque
# def solution(N, coffee_times):
#     answer = []
    
#     q = deque()
#     for index, item in enumerate(coffee_times):
#         q.append([index+1, item])

#     machines = []

#     for i in range(N):
#         machines.append(q.popleft())

#     while len(answer) != len(coffee_times):
#         done = []
#         rm = []
#         machines.sort(key=lambda x : (x[1], x[0]))
#         std = machines[0][1]

#         for index in range(N):
#             if index >= len(machines):
#                 break
#             if machines[index][1] == std:
#                 done.append(machines[index][0])
#                 rm.append(index)
#             machines[index][1] -= std
        
#         for index in sorted(rm, reverse=True):
#             del machines[index]
#             if q:
#                 machines.append(q.popleft())

#         done.sort()
#         answer.extend(done)

#     print(answer)

# """
# from collections import deque
# import heapq
# def solution(N, coffee_times):
#     answer = []

#     q = deque()
#     for index, item in enumerate(coffee_times):
#         q.append([index+1, item])

#     # max heap -> greedy alorithm에서 heap 사용빈도 높다
#     heap = []
#     for index in range(N-len(heap)):
#         if q:
#             p = q.popleft()
#             heapq.heappush(heap, (p[1], p[0]))
    
#     done = []
#     p = heapq.heappop(heap)
#     p = [p[1], p[0]]
#     done.append(p[0])

#     while heap:
#             p = heapq.heappop(heap)
#             result.append([p[0], p[1]])
#         print(result)
#     return result
# """

# N = 3
# coffee_times = [4, 2, 2, 5, 3]
# solution(N, coffee_times)

# ## 4번
# SELECT USER_ID FROM CARTS WHERE ID IN (SELECT CART_ID FROM CART_PRODUCTS WEHRE NAME = 'Flour') GROUP BY USER_ID ORDER BY USER_ID ASC