https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/math/floor_sum.cpp

# Floor Sum
`T floor_sum(T n, T m, T a, T b)`
- 인자
  - `n`은 0 이상의 정수, `m`은 양의 정수, `a`, `b`는 0 이상의 정수입니다.
  - ⚠️ `a`, `b`가 음수일 때의 동작은 테스트해보지 않았습니다.
- 동작
  - `i = 0, ..., n-1`에 대해 `floor((ai+b)/m)`의 합을 반환합니다.
- 시간 복잡도: O(logm)

# 테스트 문제
- [LC Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)
- [AtCoder practice2-C Floor Sum](https://atcoder.jp/contests/practice2/tasks/practice2_c)
- [BOJ 8483 Earthquake](https://www.acmicpc.net/problem/8483)
- [BOJ 16998 It's a Mod, Mod, Mod, Mod World](https://www.acmicpc.net/problem/16998)

다음은 LC Sum of Floor of Linear에서의 사용 예시입니다. [채점 결과](https://judge.yosupo.jp/submission/107083)

```cpp
int main(){OJize();
	int T; cin>>T;
	while(T--){
		ll n,m,a,b; cin>>n>>m>>a>>b;
		cout << floor_sum(n,m,a,b) << '\n';
	}
}
```

