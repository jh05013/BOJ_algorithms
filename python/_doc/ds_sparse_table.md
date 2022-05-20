https://github.com/jh05013/BOJ_algorithms/blob/master/python/ds/sparse_table.py

`f^i(x)`를 다음과 같이 정의합시다.

- `f^0(x) = x`
- `f^(i+1)(x) = f(f^i(x))`

이때 `f^i(x)`를 효율적으로 계산하는 자료 구조입니다.

# 선언
- `SparseTable(mmax, arr)`는 `f(x) = arr[x]`인 함수 `f`와 `0 <= i <= mmax`인 `i`에 대해 `f^i(x)`를 계산할 수 있는 sparse table을 선언합니다.

# 연산
아래에서 서술하는 모든 연산의 시간 복잡도는 O(log mmax)입니다.
- `query(i, x)`는 `f^i(x)`를 반환합니다.
- `bin_search_min(x, cond)`는 `cond(f^i(x))`가 참인 최소의 i를 반환합니다. 그런 `i <= mmax`가 없을 경우 None을 반환합니다. 이때, **cond는 아래의 조건을 만족해야 합니다.** 그렇지 않으면 UB입니다.
  - 조건: 모든 `x`에 대해, `cond(x)`가 참일 경우 `cond(f(x))`도 참이다.

# 테스트 문제
[BOJ 17435 합성함수와 쿼리](https://www.acmicpc.net/problem/17435)

아래는 합성함수와 쿼리에서의 사용 예시입니다.

```python
import sys;input=lambda:sys.stdin.readline().strip('\n')
MIS = lambda: map(int,input().split())

m = int(input())
SA = SparseTable(500000, [0] + list(MIS()))
for QUERY in range(int(input())):
    n, x = MIS()
    print(SA.query(n, x))
```