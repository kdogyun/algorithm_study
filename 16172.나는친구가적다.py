import sys
sys.stdin = open("test.txt", "r")
input = lambda : sys.stdin.readline().rstrip()

S = input()
K = input()

def getTable(pattern):
    table = [0 for i in range(len(pattern))]
    prefix_index = 0
    for suffix_index in range(1, len(pattern)):
        while prefix_index > 0 and pattern[suffix_index] != pattern[prefix_index]:
            prefix_index = table[prefix_index - 1]
        if pattern[suffix_index] == pattern[prefix_index]:
            prefix_index += 1
            table[suffix_index] = prefix_index
    return table

def kmp(s, p):
    ans = [] # 해당 패턴과 일치하는 부분의 시작점을 담는 리스트
    table = getTable(p)
    n = len(s); m = len(p); j = 0
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]
        if s[i] == p[j]:
            if j == m-1:
                ans.append(i-m+1)
                j = table[j] # j는 마지막으로 매치 되는 문자열의 위치를 가리킨다.
            else:
                j += 1
    return ans

import re
no_num = re.compile('[^0-9]')
S = ''.join(no_num.findall(S))
print(int(len(kmp(S, K)) != 0))