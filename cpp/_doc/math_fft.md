FFT입니다.

cf. [modpoly](https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/_doc/math_modpoly.md)

# Simple
https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/math/fft.cpp

`vector<T> polymul<T, DT>(vector<T> X, vector<T> Y)`
- 인자
  - `X`와 `Y`는 정수 배열입니다.
- 동작
  - `X`와 `Y`의 convolution을 반환합니다.
- 시간 복잡도: O(nlogn)

# Dual
TODO

# 수의 범위
⚠️ 충분한 실험을 거치지 않았습니다.

수의 범위가 특정 한도 이내여야 안전합니다. 다음은 각 코드의 사용 권장 범위입니다. 이때 `x`는 인자로 주어지는 배열의 원소들 중 최대 절댓값입니다.
- **Simple, int + double**: `nx^2 <= 10^9`
- **Simple, long long + long double**: `nx^2 <= 10^13`

다음 코드로 실험했습니다.

```
int main(){OJize();
	int n, mx; cin>>n>>mx;
	vector<int> X(n), Y(n);
	for(int i=0; i<n; i++) X[i] = rand()%mx;
	for(int i=0; i<n; i++) Y[i] = rand()%mx;
	polymul<int, double>(X, Y);
	cout<<n*mx*mx;
}
```

Convolution 결과의 소수 부분이 [0.2, 0.8] 범위에 있으면 RTE를 띄우도록 했습니다. 더 과감하게 FFT를 시도하시려면 `polymul` 함수의 `assert(abs(A[i].real() - res[i]) < 0.2)`을 주석 처리하십시오.

# 테스트 문제
- [BOJ 10531 Golf Bot](https://www.acmicpc.net/problem/10531) simple, int

코드 생략

- [BOJ 25456 궁금한 시프트](https://www.acmicpc.net/problem/25456) simple, int

532 ms, 86 MB

```cpp
int main(){OJize();
	vector<int> X, Y;
	string s; cin>>s;
	for(char c: s) X.push_back(c - '0');
	cin>>s;
	for(int i=0; i<2; i++) for(char c: s) Y.push_back(c - '0');
	reverse(entire(X));

	X = polymul<int, double>(X, Y);
	cout << *max_element(entire(X));
}
```
