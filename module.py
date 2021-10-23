a = [1,2,3,4,5]

a = sorted(a) #오름차순 정렬
a = sorted(a, reverse=True) #내림차순 정렬



#find / index
a = '12345555'
a.find('5') #5가 찾아지는 첫번째 위치

a = [1,2,3,4,5,5,5,5,5,5]
a.index(5) #5가 있는 첫번째 index 값
a.index(5, start, end)

import re
# 정규식으로 찾기
# .#아ㅣ;ㅓㅏㅣㄹㄴ어리ㅏㄴ얼
