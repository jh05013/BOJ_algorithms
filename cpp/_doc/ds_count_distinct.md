https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/data_structure/count_distinct.cpp

범위 안에 있는 서로 다른 수의 개수를 효율적으로 구하는 자료구조입니다. [다음 링크](http://www.secmem.org/blog/2021/07/19/distinct-value-query/)를 참조했습니다.

# 선언
- const int `CDSZ`와 `CDCNT`는 기본값이 각각 400과 2500이고, 수정이 필요할 경우 직접 코드에서 수정하여야 합니다.
- `CountDistinct(vector<T> arr)`은 내용물이 `arr`인 CountDistinct 자료구조를 선언합니다.
  - `arr`의 크기 `n <= CDSZ * CDCNT`여야 합니다.
  - 선언의 시간 복잡도는 O(nlogn + CDCNT^2)입니다.

# 연산
- `query(int l, int r)`은 `arr[l], ..., arr[r]` 중 서로 다른 수의 개수를 반환합니다.
  - 시간 복잡도는 O(CDSZ)입니다.

# 상수 조정
TODO

# 테스트 문제
- [BOJ 14898 서로 다른 수와 쿼리 2](https://acmicpc.net/problem/14898)

다음은 BOJ 14898에서의 사용 예시입니다. `CDSZ`와 `CDCNT`가 기본값일 때 메모리 135 MB, 시간 2.5초가 소요됩니다.
```cpp
int main(){OJize();
	int n; cin>>n;
	vector<int> arr(n);
	for(int i=0; i<n; i++) cin>>arr[i];
	CountDistinct<int> CD(arr);
	int pans = 0, Q; cin>>Q;
	while(Q--){
		int l,r; cin>>l>>r;
		l+= pans;
		pans = CD.query(l-1, r-1);
		cout << pans << '\n';
	}
}
```

