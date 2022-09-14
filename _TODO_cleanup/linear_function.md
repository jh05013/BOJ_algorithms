https://github.com/jh05013/BOJ_algorithms/blob/master/cpp_math/linear_function.cpp

일차함수 타입입니다. int, double, [modint](https://github.com/jh05013/BOJ_algorithms/wiki/modint-%28cpp%29) 등 사칙연산을 지원하는 타입에 대해 사용할 수 있습니다.

## Declaration
- `Linear()`은 `0x + 0`을 반환합니다.
- `Linear(b)`는 `0x + b`를 반환합니다.
- `Linear(a, b)`는 `ax + b`를 반환합니다.

## Methods
- 입력, 출력, 비교, 사칙연산을 지원합니다.
  - 입력은 stdin으로부터 `a`와 `b`를 차례로 입력받습니다.
  - 곱셈은 두 일차함수의 곱에서 `x^2` 항을 제거한 것, 즉 `f*g modulo x^2`를 반환합니다.
  - 나눗셈은 `h*g == f`인 일차함수 `h`를 반환합니다. **나눗셈이 정확하게 정의된 타입에 대해서만 사용하세요.** 그렇지 않으면 UB입니다. 예를 들어, `Linear<int>`의 나눗셈을 하면 안 됩니다.
- `composite(f, g)`는 `h(x) = f(g(x))`인 일차함수 `h`를 반환합니다.