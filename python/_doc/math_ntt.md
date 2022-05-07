https://github.com/jh05013/BOJ_algorithms/blob/master/python/math/ntt.py

Number-theoretic transform을 정의합니다.

# NTT
`poly_mul(P, Q)`
- `int`형의 전역 변수 `MOD, proot, iproot`가 필요합니다. `proot`는 MOD의 원시근, `iproot`는 `proot`의 곱셈의 역원입니다.
- 인자
  - `P`와 `Q`는 다항식으로, `[상수, x의 계수, x^2의 계수, ...]` 형태의 배열로 주어집니다. 두 다항식의 차수의 합은 n입니다.
- 동작
  - 다항식 `PQ`를 반환합니다.
- 시간 복잡도: O(n logn)
