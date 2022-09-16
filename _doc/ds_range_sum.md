https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/data_structure/range_sum.cpp

배열 `A`의 구간 합을 구하는 자료구조입니다.

# 선언
- `RangeSum(int N)`은 크기 `N`의, 모든 `A[i] = 0`인 구간 합 자료구조를 선언합니다.
- `RangeSum(vector<T> A)`는 배열 A에 대한 구간 합 자료구조를 선언합니다. 이때 `enter` 연산은 사용할 수 없습니다.

# 필드
- `n`은 배열 A의 크기입니다.

# 연산
모든 연산의 시간복잡도는 amortized `O(1)`입니다.
- `enter(int i, T x)`는 `A[i] = x`로 둡니다.
  - `0 <= i < n`이어야 합니다. 안 그러면 RTE입니다.
  - `i` 값은 가장 최근에 호출한 `enter`의 `i` 값보다 커야 하며, 지금까지 호출되었던 모든 `sum`의 `r` 값보다 커야 합니다. 안 그러면 RTE입니다.
- `sum(int l, int r)`은 `A[l] + ... + A[r]`입니다.
  - `0 <= l <= r < n`이어야 합니다. 안 그러면 RTE입니다.

# 테스트 문제
- [BOJ 11659 구간 합 구하기 3](https://acmicpc.net/problem/11659)
- [LC Static Range Sum](https://judge.yosupo.jp/problem/static_range_sum)
- [BOJ 16139 인간-컴퓨터 상호작용](https://www.acmicpc.net/problem/16139)

다음은 LC Point Add Range Sum에서의 사용 예시입니다. [채점 결과](https://judge.yosupo.jp/submission/104681)
```cpp
int main(){OJize();
	int n, Q; cin>>n>>Q;
	vector<ll> arr(n);
	for(int i=0; i<n; i++) cin>>arr[i];
	RangeSum RS(arr);
	while(Q--){
		int l, r; cin>>l>>r;
		cout << RS.sum(l, r-1) << '\n';
	}
}
```

이렇게도 사용할 수 있습니다. [채점 결과](https://judge.yosupo.jp/submission/104682)
```cpp
int main(){OJize();
	int n, Q; cin>>n>>Q;
	RangeSum<ll> RS(n);
	for(int i=0; i<n; i++){
		ll x; cin>>x;
		RS.enter(i, x);
	}
	while(Q--){
		int l, r; cin>>l>>r;
		cout << RS.sum(l, r-1) << '\n';
	}
}
```

다음은 BOJ 16139 인간-컴퓨터 상호작용에서의 사용 예시입니다. [채점 결과](https://www.acmicpc.net/source/share/8aea43f883c342b7bc5db32499037988)
```cpp
int main(){OJize();
	string s; cin>>s;
	vector<RangeSum<int>> RS(26, RangeSum<int>(sz(s)));
	for(int i=0; i<sz(s); i++) RS[s[i]-'a'].enter(i, 1);

	int Q; cin>>Q;
	while(Q--){
		char c; int l, r; cin>>c>>l>>r;
		cout << RS[c-'a'].sum(l, r) << '\n';
	}
}
```