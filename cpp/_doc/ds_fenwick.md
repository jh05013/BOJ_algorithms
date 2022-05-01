https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/data_structure/fenwick.cpp

펜윅 트리입니다.

# 필드
- `vector<T> content` - 구간 합이 아닌 원래의 내용물을 담는 vector입니다.

# 선언
- `Fenwick(int n)`은 `content`의 크기가 n인 펜윅 트리를 선언합니다.

# 연산
아래에서 서술하는 모든 연산의 시간 복잡도는 O(logn)입니다.

## 업데이트
- `add(int i, T val)`은 `content[i]`에 `val`을 더합니다.
- `change(int i, T val)`은 `content[i]`의 값을 `val`로 바꿉니다.

## 쿼리
- `sum(int i)`는 `content[0] + ... + content[i]`입니다.
- `sum(int i, int j)`는 `content[i] + ... + content[j]`입니다.
- `kth(int k)`는, **모든 content[i]가 0 이상**이라는 가정 하에, `content[0] + ... + content[i] >= k`인 최소의 i입니다. 그러한 i가 없으면 RTE입니다.

# 테스트 문제
- [BOJ 2042 구간 합 구하기](https://acmicpc.net/problem/2042) change, sum
- [LC Point Add Range Sum](https://judge.yosupo.jp/problem/point_add_range_sum) add, sum
- [BOJ 12899 데이터 구조](https://acmicpc.net/problem/12899) add, kth

다음은 LC Point Add Range Sum에서의 사용 예시입니다. [채점 결과](https://judge.yosupo.jp/submission/88011)
```cpp
int main(){OJize();
	int n, Q; cin>>n>>Q;
	Fenwick<ll> F(n);
	for(int i=0; i<n; i++){
		ll x; cin>>x;
		F.add(i, x);
	}
	while(Q--){
		ll qty, a, b; cin>>qty>>a>>b;
		if(qty == 0) F.add(a, b);
		else cout << F.sum(a, b-1) << '\n';
	}
}
```

다음은 BOJ 12899 데이터 구조에서의 사용 예시입니다. 채점 결과: 860 ms, 18412 KB
```cpp
int main(){OJize();
	int Q; cin>>Q;
	Fenwick<int> F(2000001);
	while(Q--){
		int qty, x; cin>>qty>>x;
		if(qty == 1){F.add(x, 1); continue;}
		int v = F.kth(x); F.add(v, -1);
		cout << v << '\n';
	}
}
```