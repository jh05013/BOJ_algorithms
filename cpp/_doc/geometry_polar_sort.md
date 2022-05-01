https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/geometry/polar_sort.cpp

점의 각도 정렬 관련 함수를 정의합니다.

# Polar sort
`void polar_sort(vector<Pnt<T>> &P, Pnt<T> c)`
- 인자
  - `P`는 정렬할 점의 vector입니다. 길이는 n입니다. c와 같은 점이 존재하면 assertion fail입니다.
  - `c`는 정렬의 기준이 되는 점입니다.
- 동작
  - `P`의 점들을 `c`를 기준으로 반시계 방향으로 정렬합니다.
  - `P`에서 맨 처음에 오는 점은 `c`를 기준으로 -x축에서 반시계방향으로 재었을 때, 각도가 양수이면서 가장 작은 점입니다.
  - 각도가 같을 경우, `c`에서의 거리가 작을수록 먼저 옵니다.
- 시간 복잡도: O(nlogn)

# Halfplanes for polar-sorted points
⚠️ 한 문제 이상에서 잘 돌아감을 확인했으나, 충분한 테스트가 이루어지지는 않았습니다.

`vector<int> polar_sorted_halfplanes(vector<Pnt<T>> &P, const Pnt<T> &c)`
- 인자
  - `P`는 정렬할 점의 vector입니다. 길이는 n입니다. c와 같은 점이 존재하면 assertion fail입니다.
  - `c`는 정렬의 기준이 되는 점입니다.
  - P는 `c`를 기준으로 반시계 방향으로 정렬되어 있어야 합니다. 그렇지 않으면 UB입니다.
- 동작
  - 길이가 n인 vector `R`을 반환합니다.
  - `R[i] < n`일 경우, `P[i], P[i+1], ..., P[R[i]]`는 모두 한 반평면 내에 있습니다. 이때 "반평면 내"는 경계도 포함합니다.
  - `R[i] >= n`일 경우, `P[i], P[i+1], ..., P.back(), P[0], ..., P[R[i]-P.size()]`는 모두 한 반평면 내에 있습니다.
- 시간 복잡도: O(n)

# 테스트 문제
- [LC Sort Points by Argument](https://judge.yosupo.jp/problem/sort_points_by_argument)

아래는 LC Sort Points by Argument에서의 사용 예시입니다. [채점 결과](https://judge.yosupo.jp/submission/88002)
```cpp
int main(){OJize();
	int n; cin>>n;
	vector<Pnt<ll>> P;
	int origins = 0;
	for(int i=0; i<n; i++){
		Pnt<ll> p; cin>>p;
		if(p != Pnt<ll>()) P.push_back(p);
		else origins++;
	}
	polar_sort(P, Pnt<ll>());
	for(auto p: P){
		if(p.y >= 0) while(--origins >= 0) cout<<"0 0\n";
		cout<<p.x<<' '<<p.y<<'\n';
	}
}
```