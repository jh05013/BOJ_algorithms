https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/math/euler_phi.cpp

# Euler Phi
`T euler_phi(T n)`
- 인자
  - `n`은 양의 정수입니다.
- 동작
  - `ϕ(n)`, 즉 `n`보다 작으면서 `n`과 서로소인 양의 정수의 개수를 반환합니다.
- 시간 복잡도: O(√n)

# 테스트 문제
- [BOJ 11689 GCD(n, k) = 1](https://www.acmicpc.net/problem/11689)
- [BOJ 4355 서로소](https://www.acmicpc.net/problem/4355)

다음은 BOJ 11689에서의 사용 예시입니다.

```cpp
int main(){OJize();
	while(1){
		int n; cin>>n;
		if(n == 0) break;
		else cout << euler_phi(n) << '\n';
	}
}
```

