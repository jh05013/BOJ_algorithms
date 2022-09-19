https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/math/modint.cpp

특정 상수 `MOD`를 모듈로 값으로 갖는 다항식 타입입니다. `MOD`는 기본값이 998,244,353이고, `PRIMITIVE_ROOT`는 기본값이 3입니다. 필요에 따라 바꿔서 사용하되, number-theoretic transform이 가능하도록 설정하십시오.

# 필드
- `vector<modint> P`는 순서대로 상수항, x의 계수, x^2의 계수, ...을 담고 있습니다.

# 선언
- `modint<T>(int n)`
- `modint<T>(vector<modint> A)`

# 연산
## 입출력
- `cin >>`으로 `P[0]`부터 `P[n-1]`까지 입력받을 수 있습니다.
- `cout <<`으로 `P[0]`부터 `P[n-1]`까지 출력할 수 있습니다.

## 기본 연산
- TODO 덧셈, 뺄셈 넣기
- 곱셈을 지원합니다. FFT를 사용하며 시간 복잡도는 `O(nlogn)`입니다.

# 테스트 문제
[LC Convolution](https://judge.yosupo.jp/problem/convolution_mod) ([채점 결과](https://judge.yosupo.jp/submission/104699))
```cpp
int main(){
	ll n; cin>>n;
	ll ans = 0;
	for(auto [x, l, r]: harmonic_ceil(n)) ans+= x*(r-l+1);
	cout << ans+1;
}
```

