https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/math/harmonic_lemma.cpp

양의 정수 n에 대해 floor(n/i)로 가능한 값은 O(sqrt(n))개 존재함이 알려져 있습니다. 이 값들을 얻어내는 함수를 정의합니다.

# One number version
`vector<tuple<T,T,T>> harmonic_floor(T n)`
- 인자
  - `n`은 양의 정수입니다. 정수가 아니면 UB입니다. 양수가 아니면 RTE입니다.
- 동작
  - 튜플 `(x, l, r)`로 이루어진 vector를 반환합니다.
  - 각 `(x, l, r)`은 `floor(n/i) = x`인 `i`의 범위가 구간 `[l, r]`이라는 의미입니다. `x`에 대한 내림차순으로 정렬되어 있으며, `[l, r]`이 비어있지 않으면서 `x >= 1`인 튜플만 vector에 들어있습니다.
- 시간 복잡도: O(sqrt(n))

`vector<tuple<T,T,T>> harmonic_ceil(T n)`은 위와 같으나, `ceil(n/i)`를 사용하며, `x >= 2`인 튜플만 vector에 들어있습니다.

# Two numbers version
`vector<tuple<T,T,T,T>> harmonic2_floor(T n, T m)`
- 인자
  - `n`과 `m`은 양의 정수입니다. 정수가 아니면 UB입니다. 양수가 아니면 RTE입니다.
- 동작
  - 튜플 `(x, y, l, r)`로 이루어진 vector를 반환합니다.
  - 각 `(x, y, l, r)`은 `floor(n/i) = x, floor(m/i) = y`인 `i`의 범위가 구간 `[l, r]`이라는 의미입니다.
- 시간 복잡도: O(sqrt(n))

TODO implement `harmonic2_ceil`

# 테스트 문제
- [BOJ 15897 잘못 구현한 에라토스테네스의 체](https://www.acmicpc.net/problem/15897) one ceil

아래는 BOJ 15897 잘못 구현한 에라토스테네스의 체에서의 사용 예시입니다. 채점 결과: 4 ms, 4452 KB

```cpp
int main(){
	ll n; cin>>n;
	ll ans = 0;
	for(auto [x, l, r]: harmonic_ceil(n)) ans+= x*(r-l+1);
	cout << ans+1;
}
```
