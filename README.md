# algorithm_study

2020년 11월부터 파이썬을 이용한 알고리즘 공부로 변경.

(포스코 청년 AI/BigData 아카데미에서 알고리즘 스터디를 계기로 제대로 된 스터디를 시작함.)

2020/11 부터 '상규'님을 필두로 알고리즘 스터디를 시작했으나, 카카오 입사로 인해 나가게 됨.

현재는 녹형님이 이끄시는 알고리즘 스터디로 운영이 되고 있음.

그 외에도 현재 '논문 스터디 4인조'와 함께 기본 알고리즘 스터디를 운영 중.

<u>***목표는 카카오 코데!!***</u>



### 2020/01/12

- sort_bubble
- sort_insert
- sort_quick
- sort_select
- search_binary



### 2020/12/26

**이분탐색** 7문제중 3문제 맞춤.

- 1920.수찾기 :heavy_check_mark:

  이분탐색 클래스를 만들어서 구현.

  시간복잡도가 꽤 높게 나오던데 수정이 필요해 보임..

- 2805.나무자르기 :x:

  ~~어떻게 접근해야할지 감이 서지 않음.~~

  ~~왜.... 이분탐색인거지? 어째서?~~

  > 2020.12.27(일) 스터디에서 알게된 접근법.
  >
  > 제일 큰 나무를 기준으로 중간값을 구해서 잘라서 조건에 만족하는지 구하고, 만약에 모자라다면 mid값을 아래쪽으로 찾아주고, 많다면 mid값을 위로 찾아준다. (이분탐색)

- 10815.숫자카드 :x:

  1920번과 동일하게 클래스로 구현한 이분탐색을 이용해서 삽입 & 검색 구현.

  하지만 시간초과... pypy3으로 해도 시간 초과...

  이분탐색 알고리즘을 수정이 필요.

  > 2020.12.27(일) 스터디에서 알게된 해결법.
  >
  > 없습니다... 백준 질문하기에서 물어보는 걸로...
  >
  > 2020.01.02(토) 백준 질문 답변
  >
  > 이분탐색을 내가 직접 구현한게.. list sort보다 느리다고 합니다..ㅠㅠ

- 1654.랜선자르기 :x:

  전체 랜선 길이 합을 필요한 랜선길이 만큼 나눈 값을 구한다. 그 값과 최대 반올림(252면 10의 자리에서 반올림해서 100자리 수만 남김)을 해 그 구간만큼 반복문을 돌려, 그 길이로 잘랐을때 나오는 count가 원하는 갯수와 같으면 최대 길이를 업데이트해줌.

  ~~접근 방법이 잘못됐나봄... 틀리거나 시간초과가 뜸.~~

  > 2020.12.27(일) 스터디에서 알게된 접근법.
  >
  > 나무자르기와 동일하게 접근.

- 10816.숫자카드2 :heavy_check_mark:

  딕셔너리를 이용함.

  원래는 이것도 이진트리를 이용해서 이진탐색을 해야할 것 같았으나, 딕셔너리를 이용하면 쉽고 빠르게 찾을 수 있어 이용해보니 맞았음.

  이진탐색으로는 어떻게 구현하는걸까?

  > 2020.12.27(일) 스터디에서 알게된 다른 풀이.
  >
  > C++에서는 map을 이용해서 풀이.

- 1764.듣보잡 :heavy_check_mark:

  딕셔너리를 이용함.

  이것도 이진트리를 이용해서 처음에 삽입하고 후에 검색을 하여 그 결과값을 또 이진트리에 넣으면서 오름차순으로 정렬하여 출력해줘야 하는 것 같았으나, 딕셔너리를 이용해 검색하고 결과값만 리스트에 넣어 sort시켜 출력.

  이진탐색으로는 어떻게 구현하는걸까?

- 2512.예산 :x:

  모든 예산을 받아 오름차순으로 정렬하여, 하나씩 빼보면서 최대 상한선을 구해 나머지값(주어진 예산에서 얼마가 남는지) 과 비교하여 최대상한선을 정해줌.

  시간초과.
  
  > 2020.12.27(일) 스터디에서 알게된 접근법.
  >
  > 나무자르기와 동일하게 접근.



### 2020/01/02

**우선순위 큐 (힙큐)** 7문제 중 4문제 맞춤

- 1927.최소힙 :heavy_check_mark:

  최소 힙 class로 구현함.

  배열에 넣어두고 부모는 자식 위치의 1/2라는 것을 이용해서 작성.

- 2014.소수의곱 :x:

  최소힙에 넣어두고, 최소값을 하나 꺼낸 후 기존에 받았던 번호에 곱해서 중복 제거해 준 후에 다시 힙에 넣는다. 이것을 원하는 횟수까지 반복.

  ***메모리 및 시간 터짐***

- 2865.나는위대한슈퍼스타K :heavy_check_mark:

  각 사람별 최대힙을 구한 후, 최대값만 리스트에 저장하여 본선에 올라온 수만큼만 더해줌.

  > 나는 최대힙으로 구현했지만, 다른 사람을 보니 그냥 리스트에 최대값만을 저장해두는 방식으로 해서 메모리를 절약하는 방법이 있었음.

- 14241.슬라임합치기 :heavy_check_mark:

  최대힙으로 구현을 하면되지만, 클래스를 구현하기 귀찮아서 리스트에 sort함수를 적용시켜 문제를 품.

- 17503.맥주축제 :x:

  (선호도, 알코올) 쌍으로 리스트에 입력받아 선호도 기준 오름차순, 알코올 기준 내림차순으로 정렬하여 앞에서부터 선호도를 갯수만큼 합하여 나오지 않으면 최소 선호도를 삭제하는 방식으로 접근함.

  여기서 문제점은 최대+최소 조합으로도 가능한데 이렇게 접근하면 안된다는 것임...

- 1715.카드정렬하기 :heavy_check_mark:

  최소힙을 구현하기 귀찮아 슬라임처럼 list에 sort를 적용하여 풀려고 하였으나, 시간초과가 뜸. 최소힙을 구현해서 품.

- 1655.가운데를말해요 :x:

  리스트에 넣고 항상 가운데 값, 짝수면 중간에 있는 두개의 값을 비교해서 출력하는 걸로 접근.

  ***시간 터짐***



### 2021/01/05

**부스트 캠프 AI 2차 코딩테스트** 준비를 위해 실버 1~2정도 난이도 3문제 골라서 1시간안에 풀기!!

는 0솔...ㅠㅠ

- 1695.숨바꼭질 :x:

  라인 2019 코테 기출과 유사

  너무 어렵게 접근함... 스터디 멤버 접근법을 보면 BFS로 충분... 1차 코테에서 개구리 점프랑 동일함....

- 2293.동전1 :x:

  DP문제인데...

  점화식도 점화식인데 반복문을 어떻게 쓰느냐에 따라 완전 달라짐... 접근법이 떠오르지 않음..

- 2318.전구와스위치 :x:

  접근 불가...

  끝판왕인듯... 생각해내는 사람 미친.. 괴물입니다....




#### 현재까지의 성과

2020.12.26

BFS로 문제를 해결 할 수 있게 됨.

위상정렬과 투포인터 알고리즘 해결법과 문제를 이해할 수 있게 됨.

이분탐색을 이해하고 문제 접근법에 대해 이해함.

하지만 여전히 DP문제와 시뮬레이션 문제는 어려움...

2021.01.02

우선순위 큐(힙큐)에 대해서 이해함.