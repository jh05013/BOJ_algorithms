https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/math/modint.cpp

특정 상수 `MOD`를 모듈로 값으로 갖는 정수 타입입니다. `MOD`는 기본값이 1,000,000,007입니다. 필요에 따라 다른 값으로 바꿔 사용하십시오.

# 필드
- `T val`

# 선언
- `modint<T>()`은 0입니다.
- `modint<T>(ll v)`는 v를 `MOD`로 나눈 나머지입니다.

# 연산
## 입출력
- `cin >>`으로 val을 입력받을 수 있습니다.
- `cout <<`으로 val을 출력할 수 있습니다.

## 기본 연산
- `MOD` 상수가 같은 두 modint의 사칙연산 및 비교를 지원합니다.
  - **나눗셈은 `MOD`가 소수일 때만 사용하세요.** 그렇지 않으면 UB입니다.
  - `a / b`의 시간 복잡도는 O(log`MOD`)입니다.
- `inv(a)`는 `1 / a`를 반환합니다. 시간 복잡도는 O(log`MOD`)입니다.
- `ipow(a, p)`는 `a`의 `p`제곱을 반환합니다. 시간 복잡도는 O(log p)입니다.