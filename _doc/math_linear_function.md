https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/math/linear_function.cpp

일차함수 타입입니다. int, double, [modint](https://github.com/jh05013/BOJ_algorithms/wiki/modint-%28cpp%29) 등 사칙연산을 지원하는 타입에 대해 사용할 수 있습니다.

# 필드
- `T a`
- `T b`

# 선언
- `Linear<T>()`은 `0x + 0`입니다.
- `Linear<T>(T b)`는 `0x + b`입니다.
- `Linear<T>(T a, T b)`는 `ax + b`입니다.

# 연산
## 입출력
- `cin >>`으로 a, b를 입력받을 수 있습니다.
- `cout <<`으로 일차식을 출력할 수 있습니다. 계수가 0인 항은 출력되지 않으며, `x`의 계수가 1이면 계수가 출력되지 않습니다.

## 기본 연산
- 두 일차함수의 사칙연산 및 비교(같음과 다름)를 지원합니다.
  - 곱셈은 `x^2` 항을 제거한 것, 즉 `f*g modulo x^2`를 반환합니다.
  - 나눗셈은 `h*g modulo x^2 == f`인 일차함수 `h`를 반환합니다. **나눗셈이 정확하게 정의된 타입에 대해서만 사용하세요.** 그렇지 않으면 UB입니다. 예를 들어, `Linear<int>`의 나눗셈을 하면 안 됩니다.
- `composite(f, g)`는 `h(x) = f(g(x))`인 일차함수 `h`를 반환합니다.