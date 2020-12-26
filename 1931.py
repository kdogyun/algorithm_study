n = int(input())
meeting_list = []

for i in range(n):
    start, end = map(int, input().split())
    meeting_list.append((start, end))

for meeting in meeting_list:
    