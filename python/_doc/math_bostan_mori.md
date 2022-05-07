https://github.com/jh05013/BOJ_algorithms/blob/master/python/math/bostan_mori.py

길이 d의 선형 점화식으로 만들어지는 수열의 n번째 항을 MOD로 나눈 나머지를 구하는 알고리즘입니다. 기반이 되는 논문은 [Bostan, Mori. A Simple and Fast Algorithm for Computing the N-th Term of a Linearly Recurrent Sequence](https://arxiv.org/abs/2008.08822)입니다.

사용하려면 두 다항식을 곱하는 `poly_mul(P, Q)` 함수가 정의되어 있어야 합니다. 이때, 다항식은 `[상수항, x의 계수, x^2의 계수, ...]`의 형태로 주어집니다.

# Bostan-Mori algorithm
`bostan_mori(s)`
- `int`형의 전역 변수 `MOD`가 필요합니다.
- 인자
  - `C`는 길이가 d인 점화식입니다. `A[0], ..., A[d-1]`이 주어졌을 때, `A[d]`는 `A[0]*C[0] + ... + A[d-1]*C[d-1]`로 계산됩니다.
  - `ini`는 초항 `A[0], A[1], ...`입니다. 길이는 d 이하여야 합니다. **길이가 d보다 클 경우는 테스트해보지 않았습니다.**
  - `n`은 값을 구할 항의 번호입니다.
- 동작
  - `A[n]`을 `MOD`로 나눈 나머지를 반환합니다.
- 시간 복잡도: O(M(d) logn). 이때 M(d)는 길이가 d인 두 다항식을 곱하는 `poly_mul` 함수의 시간 복잡도입니다.

# 테스트 문제
- [Codechef RNG](https://www.codechef.com/problems/RNG)

아래는 RNG에서의 사용 예시입니다. [채점 결과](https://www.codechef.com/viewsolution/64429496)

```python
MOD = 104857601
proot = 3
iproot = pow(proot, MOD-2, MOD)

def NTT(N, X, di):
    ...

def poly_mul(P, Q):
    ...

k, n = MIS()
A = list(MIS())
C = list(MIS())[::-1]
print(bostan_mori(C, A, n-1))
```