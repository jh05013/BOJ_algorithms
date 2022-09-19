https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/etc/max_sumarray.cpp

`T max_sumarray(vector<T> arr)`은 `arr`의 비어있지 않은 연속한 부분수열 중 최대 합을 반환합니다.
- `arr`이 비어있으면 RTE입니다.
- 시간 복잡도: `O(n)`

# 테스트 문제
- [BOJ 1912 연속합](https://www.acmicpc.net/problem/1912)

8 ms, 3588 kB

```cpp
int main(){OJize();
	int n; cin>>n;
	vector<ll> A(n); for(auto &x: A) cin>>x;
	cout << max_sumarray(A);
}
```
