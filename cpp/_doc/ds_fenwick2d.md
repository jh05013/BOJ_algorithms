https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/data_structure/fenwick2d.cpp

이차원 펜윅 트리입니다.

# 선언
- `Fenwick2d(int n, int m)`은 `content`의 크기가 n*m인 펜윅 트리를 선언합니다.

# 필드
- `vector<vector<T>> content` - 구간 합이 아닌 원래의 내용물을 담는 vector입니다.

# 연산
아래에서 서술하는 모든 연산의 시간 복잡도는 `O(logn)`입니다.

**업데이트**
- `add(int i, int j, T val)`은 `content[i][j]`에 `val`을 더합니다.
- `change(int i, int j, T val)`은 `content[i][j]`의 값을 `val`로 바꿉니다.

**쿼리**
- `sum(int i, int j)`는 모든 `0 <= x <= i, 0 <= y <= j`에 대한 `content[x][y]`의 합입니다.
- `sum(int i1, int j1, int i2, int j2)`는 모든 `i1 <= x <= i2, j1 <= y <= j2`에 대한 `content[x][y]`의 합입니다.

# 테스트 문제
- [BOJ 11658 구간 합 구하기 3](https://www.acmicpc.net/problem/11658)

18 MB, 200 ms

```cpp
int main(){OJize();
	int n, Q; cin>>n>>Q;
	Fenwick2D<ll> F(n, n);
	for(int i=0; i<n; i++) for(int j=0; j<n; j++){
		ll x; cin>>x;
		F.add(i, j, x);
	}
	while(Q--){
		int qty; cin>>qty;
		if(qty == 1){
			int i1,j1,i2,j2; cin>>i1>>j1>>i2>>j2;
			cout << F.sum(i1-1, j1-1, i2-1, j2-1) << '\n';
			continue;
		}
		int i, j; ll x; cin>>i>>j>>x;
		F.change(i-1, j-1, x);
	}
}
```