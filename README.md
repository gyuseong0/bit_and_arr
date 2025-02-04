#### 비트마스킹을 이용한 부분배열 연산에서의 dp 테크닉

---
이 테크닉은 적용범위가 굉장히 좁고 뚜렷합니다. 누구나 떠올릴 수 있지만, 분석해 볼만큼 시간이 한가로운 사람은 많지 않기에 저의 영광스러운 첫 깃허브 파일로는 안성맞춤이겠습니다.

온라인 저지에서 문제들을 풀다보면 비트마스킹을 이용해 배열의 조합탐색을 진행해야 하는 경우가 있습니다.

예를들면 [6, 11, 15, 4, 28] 같은 배열에서 부분배열 합의 모든 경우의 수를 구하기 위해 우리는 i를 00001(2) 부터 11111(2) 까지 반복문을 돌려 비트에 해당하는 값을 더한 뒤, 반영합니다. (물론 집합과 dp를 거치는 메모리는 많이 먹어도 훨씬 쾌적한 풀이가 있긴 하지만, 일단 그런갑다 하고 넘어갑시다)

깔끔해보이지만 한 가지 흠은 비트를 더하는 횟수입니다. 배열의 크기를 20 정도로 잡으면 마지막인 111...111 에 해당하는 부분배열의 합을 구하기 위해 20번의 추가적인 연산을 진행합니다. 이는 단적으로 봤을 때는 매우 적게 느껴질 수 있지만, i는 1부터 (2^20)-1 까지 증가할 겁니다. bit_count() 합은 10,485,760정도네요. 조금 과하죠?

하지만 i에 해당하는 연산을 줄일 수만 있다면 전체적인 연산 역시 그에 비례해 빠르게 줄어들겁니다.

---
#### 줄여봅시다
생각해보면 1011001에 해당하는 부분합을 구하고 싶을 때, 앞서 언급한 것처럼 배열의 0, 3, 4, 6번 인덱스 값을 더해야만 할 필요는 없습니다.
바로 직전 i인 1011000 에 해당하는 부분합에서 배열의 0번 인덱스 값을 더해주기만 하면 됩니다.

마찬가지로 1011010에 해당하는 부분합 역시 직전 i인 1011001 에 해당하는 부분합을 이용해 구할 수 있습니다. 1번 인덱스 값은 더해주고, 0번 인덱스 값은 빼 주면 1011010 이 만들어지겠습니다. 전체적으로 이런 식입니다. 이전 합을 이용해 다음 i에 해당하는 값을 구해 나갑니다.

세 줄로 표현할 수 있습니다.
1. 이전 i 비트에 해당하는 부분합을 가져온다.
2. 현재 i를 이진수로 나타낸 값에서 가장 오른쪽에 있는 1의 위치를 구한 다음,
3. 그 위치에 해당하는 값은 이전 부분합에 더해주고, 그 위치 오른쪽에 있는 모든 0의 위치에 해당하는 값들은 이전 부분합에서 빼준다.

[4, 2, 6, 5, 3] 같은 배열에서 i = 16 에 해당하는 부분배열의 합을 구하기 위해 i = 15 에 해당하는 배열의 부분합인 17 에서 4 2 6 5을 차례대로 빼준 뒤, 4번 인덱스(가장 처음 1이 등장하는 자리)인 3를 더해준다면, 3 완성입니다.

이 방식은 i가 홀수일 때, 한 번의 연산만으로 비트에 해당하는 부분배열합을 구할 수 있다는 점이 핵심입니다.

---
#### 눈치 챘나요?
더 줄일 수 있습니다.

우선, 가장 오른쪽에 있는 1의 위치는 (i & -i).bit_length() 를 이용해 간단히 찾을 수 있구요.

어차피 이진수를 이용한 조합탐색 문제에서 배열의 크기는 커봤자 두 자릿수입니다.

위의 3번째 과정에서 각 bit_length() 위치에 해당하는 가중치를 저장한 배열을 탐색 전 만들어 두신다면...

마침내 각 i 에 해당하는 부분배열의 연산을 O(log(i)) 에서 O(1) 로 줄이는 데 성공했습니다!

---
#### 좁고 뚜렷한 적용범위
...사실 이 기술은 "알고 있어도 나쁠 건 없다" 범주를 넘지 못합니다. 

대부분의 경우 집합과 딕셔너리를 업데이트해가며 구하는 게 훨씬 빠르고, 유동적이기 때문입니다. (특히 저티어의 배낭 문제는 손쉽게 풀어넘기죠)

가끔가다 메모리적인 장점은 있겠습니다만... 다음에 더 찾아보죠.

---
#### 사전 설명 끝입니다
파일은 점차 추가될 겁니다.

bit_and_arr.py 는 위의 세 가지 방식으로 구현한 함수들의 속도 비교 코드입니다.

크기가 20인 배열을 검사할 때, 처리 시간 차이가 17배 정도 나네요 (배열의 크기가 커질수록 차이도 커질텐데 이거는 직접 수정해 보시고...)

차후 추가될 파일들은 이 테크닉으로 풀어낸 백준의 문제들입니다.

1208 - Meet In The Middle 테크닉과 결합해봤습니다. 비록 "집합과 dp를 거치는 쾌적한 풀이" 에 속도 측면에서 밀리긴 했지만, n이 40에 가까운 이런 단순무식한 문제에서 큰 힘을 발휘하는 것 같습니다.

25047 - 2차원 배열에서 적용시킨 케이스이자, 이 글을 작성한 계기이기도 합니다. 해당 테크닉 덕에 python3 문법 제출자중 유이하게 "맞았습니다!!" 를 받았습니다. (2025년 1월 23일 기준)
