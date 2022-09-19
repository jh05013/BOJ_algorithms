https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/data_structure/cartesian_tree.cpp

# 선언
- `CartesianTree(vector<T> arr)`는 `arr`의 카르테시안 트리를 선언합니다. 부모 쪽으로 올라갈 수록 값이 작아집니다.
  - 시간 복잡도: `O(n)`

# 필드
- `P`는 각 정점의 부모 정점 번호를 담는 배열입니다. 루트면 자기 자신입니다.
- `L`은 각 정점의 왼쪽 자식 정점 번호를 담는 배열입니다. 왼쪽 자식이 없으면 -1입니다.
- `R`은 각 정점의 오른쪽 자식 정점번호를 담는 배열입니다. 오른쪽 자식이 없으면 -1입니다.

# 테스트 문제
- [LC Cartesian Tree](https://judge.yosupo.jp/problem/cartesian_tree)
- 모든 "히스토그램에서 가장 큰 직사각형" 문제들

다음은 LC Cartesian Tree에서의 사용 예시입니다. [채점 결과](https://judge.yosupo.jp/submission/99003)
```cpp
int main(){OJize();
	int n; cin>>n;
	vector<int> arr(n); for(int i=0; i<n; i++) cin>>arr[i];
	CartesianTree<int> CT(arr);
	for(int x: CT.P) cout << x << ' ';
}
```
