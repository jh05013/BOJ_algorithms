https://github.com/jh05013/BOJ_algorithms/blob/master/cpp_math/z_algo.cpp

길이가 n인 `string s`에 대해, `z_algo(s)`는 다음을 만족하는 `vector<int> z`를 반환합니다.
- `z`의 길이는 n입니다.
- 각 `i`에 대해, `z[i]`는 `s`와 `s[i..]`의 최장 공통 접두사의 길이와 같습니다.

`s`가 `string`이 아니라 `vector`여야 할 경우, 둘 중 아래에 있는 함수를 사용하세요.

시간 복잡도는 O(n)입니다.

# 참고 자료
- 튜토리얼: [Z-function and its calculation](https://cp-algorithms.com/string/z-function.html) by cp-algorithms

# 테스트 문제
- [LC Z Algorithm](https://judge.yosupo.jp/problem/zalgorithm)

아래는 LC Z Algorithm에서의 사용 예시입니다. [채점 결과](https://judge.yosupo.jp/submission/85457)

```cpp
int main(){
	string s; cin>>s;
	for(int x: z_algo(s)) cout<<x<<' ';
}
```