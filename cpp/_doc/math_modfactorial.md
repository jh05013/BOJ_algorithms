https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/math/modfactorial.cpp

상수 `MOD`를 모듈로 값으로 하여 팩토리얼을 계산합니다. 사용하려면 [modint](https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/math/modint.cpp)가 필요합니다.

# 선언
- `Modfact(N) mf`는 0부터 N까지에 대해 팩토리얼을 계산하는 자료구조를 선언합니다.
  - 선언의 시간 복잡도: O(N + log MOD)

# 연산
- `mf[i]`는 `i!` mod `MOD`입니다.
  - `0 <= i < N`이어야 합니다. 안 그러면 UB입니다.
  - 시간 복잡도: O(1)
- `mf.binom(n, k)`는 `nCk`, 즉 `binom(n, k)` mod `MOD`를 반환합니다.
  - **MOD는 소수**여야 합니다. 안 그러면 UB입니다.
  - `0 <= n < N`, `0 <= k`여야 합니다. 안 그러면 UB입니다.
  - `n > k`이면 0을 반환합니다.
  - 시간 복잡도: O(1)

# 테스트 문제
[BOJ 13977 이항 계수와 쿼리](https://www.acmicpc.net/problem/13977)

```cpp
int main(){OJize();
	Modfact MF(4000001);
	int Q; cin>>Q;
	while(Q--){
		int n,k; cin>>n>>k;
		cout << MF.binom(n, k) << '\n';
	}
}
```