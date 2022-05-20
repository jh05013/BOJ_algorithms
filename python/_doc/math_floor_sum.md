https://github.com/jh05013/BOJ_algorithms/blob/master/python/math/floor_sum.py

`(a*i+b)//m`의 합을 빠르게 구합니다.

# Floor Sum
`floor_sum(n, m, a, b)`
- 인자
  - `n, m, a, b`는 `int`입니다. `0 <= n and 1 <= m`이 성립해야 합니다.
- 동작
  - `sum((a*i+b)//m for i in range(n))`을 반환합니다.
- 시간 복잡도: O(log m)

# 테스트 문제
- [AtCoder Library Practice Contest C Floor Sum](https://atcoder.jp/contests/practice2/submissions/22281032)
- [BOJ 8483 Earthquake](https://www.acmicpc.net/problem/8483)
- [BOJ 16998 It's a Mod, Mod, Mod World](https://www.acmicpc.net/problem/16998)

아래는 Floor Sum에서의 사용 예시입니다. [실행 결과](https://atcoder.jp/contests/practice2/submissions/22281032)

```python
for TEST in range(int(input())):
    n, m, a, b = MIS()
    print(floor_sum(n, m, a, b))
```