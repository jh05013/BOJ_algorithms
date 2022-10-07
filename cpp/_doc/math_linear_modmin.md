https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/math/linear_modmin.cpp

credit: [EtvycAuRLZpb6hhe86x0 에디토리얼](https://github.com/ghudegy/2021/blob/main/factorial-editorial.pdf)

# Linear Modulo Minimum
`T linear_modmin(T a, T b, T N, T e)`
- 인자
  - `a`, `b`, `N`, `e`는 음이 아닌 정수이며 `N > 0`입니다.
- 동작
  - `x` = 0, ..., `e`에 대해 `(a*x+b)%N`의 최솟값을 반환합니다.
- 시간 복잡도: O(log N)

# 테스트 문제
- [LC Min of Mod of Linear](https://judge.yosupo.jp/problem/min_of_mod_of_linear)

[채점 결과](https://judge.yosupo.jp/submission/107409)

```cpp
int main(){OJize();
	int T; cin>>T;
	while(T--){
		ll n,m,a,b; cin>>n>>m>>a>>b;
		cout << linear_modmin(a, b, m, n-1) << '\n';
	}
}
```
