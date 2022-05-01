https://github.com/jh05013/BOJ_algorithms/blob/master/cpp_math/modint.cpp

특정 상수 `MOD`를 모듈로 값으로 갖는 정수 타입입니다.

## Declaration
- `modint()`는 modint 0을 반환합니다.
- `modint(v)`는 v를 `MOD`로 나눈 값의 modint를 반환합니다.

## Methods
- 입력, 출력, 비교, 사칙연산을 지원합니다.
  - 나눗셈은 `MOD`가 소수일 때만 사용하세요. 그렇지 않으면 UB입니다.
  - `a / b`의 시간 복잡도는 O(MOD)입니다. 나머지 연산의 시간 복잡도는 O(1)입니다.
- `inv(a)`는 `1 / a`를 반환합니다. 시간 복잡도는 O(MOD)입니다.
- `ipow(a, p)`는 `a`의 `p`제곱을 반환합니다. 시간 복잡도는 O(log p)입니다.