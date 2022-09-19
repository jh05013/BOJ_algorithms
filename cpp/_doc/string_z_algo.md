https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/string/z_algo.cpp

`vector<int> z_algo(string &s)` 또는 `vector<int> z_algo(vector<T> &s)`는 길이가 n인 `vector<int> z`를 반환합니다.
- `z[i]`는 `s`와 `s[i..]`의 최장 공통 접두사의 길이와 같습니다.
- 시간 복잡도: O(n)

# 테스트 문제
- [LC Z Algorithm](https://judge.yosupo.jp/problem/zalgorithm)
- [BOJ 13713 문자열과 쿼리](https://www.acmicpc.net/problem/13713)

아래는 LC Z Algorithm에서의 사용 예시입니다. [채점 결과](https://judge.yosupo.jp/submission/85457)

```cpp
int main(){
	string s; cin>>s;
	for(int x: z_algo(s)) cout<<x<<' ';
}
```