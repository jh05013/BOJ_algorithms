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

## 연산
- 덧셈 `O(n)`
- 뺄셈 `O(n)`
- 곱셈 `O(nlogn)`
- 나눗셈 `O(nlogn)`
- 나머지 `O(nlogn)`
- `inv`: 1/P `O(nlogn)`
- `derivative`: P' `O(n)`
- `integral`: ∫P `O(nlogMOD)`
- `log`: logP `O(n(logMOD + logn))`
- `exp`: e^P `O(n(logMOD + logn))`
- `multieval`: multipoint evaluation `O(nlog^2n)`

# 테스트 문제
- [LC Convolution](https://judge.yosupo.jp/problem/convolution_mod) ([채점 결과](https://judge.yosupo.jp/submission/104699))
- [LC Inv of Formal Power Series](https://judge.yosupo.jp/problem/inv_of_formal_power_series) ([채점 결과](https://judge.yosupo.jp/submission/105294))
- [LC Division of Polynomials)(https://judge.yosupo.jp/problem/division_of_polynomials) ([채점 결과](https://judge.yosupo.jp/submission/105295))
- [LC Log of Formal Power Series](https://judge.yosupo.jp/problem/log_of_formal_power_series) ([채점 결과](https://judge.yosupo.jp/submission/105546))
- [LC Exp of Formal Power Series](https://judge.yosupo.jp/problem/exp_of_formal_power_series) ([채점 결과](https://judge.yosupo.jp/submission/105552))
- [LC Multipoint Evaluation](https://judge.yosupo.jp/problem/multipoint_evaluation) ([채점 결과](https://judge.yosupo.jp/submission/105448))
- [BOJ 18168 Game With Polynomials 2](https://www.acmicpc.net/problem/18168)
