https://github.com/jh05013/BOJ_algorithms/blob/master/cpp_ds/linkcut.cpp

이 문서에서,
- `x`, `y`는 노드 포인터입니다.
- "`x`의 전역 트리"란, 모든 간선이 포함된 포레스트 중 노드 `x`를 포함하는 트리를 의미합니다.
- "`x`의 스플레이 트리"란, 노드 `x`를 포함하는 스플레이 트리를 의미합니다. 하나의 전역 트리는 여러 개의 스플레이 트리로 이루어져 있습니다.

# `LinkCut`
## Declaration
- `LinkCut<Snode>(arr)`은 노드(`Snode`)의 개수가 `arr`의 길이와 같고, 노드의 내용물이 순서대로 `arr`의 내용물과 같으며, 아무 간선도 없는 링크/컷 트리를 만듭니다. 노드의 번호는 순서대로 0, 1, 2, ...입니다.
  - 노드의 번호를 1, 2, 3, ...으로 하려면, `arr`의 맨 앞에 아무 거나 하나 집어넣으세요.

## Fields
- `n`은 노드의 개수입니다.
- `nodes`는 모든 노드를 담은 배열입니다. `nodes[i]`의 번호는 `i`입니다.

## Methods
- `new_node(c)`는 내용물이 `c`인 새로운 노드를 만듭니다. 이 노드의 번호는 지금까지 부여되지 않은 음이 아닌 정수 중 가장 작은 값입니다.
- `input(cnt)`은 stdin으로부터 두 정수 a와 b를 받아, a번과 b번 노드를 연결하는 작업을 `cnt`번 반복합니다.
- `access(x)`는 `x`에서부터 `x`의 전역 트리의 루트까지 하나의 스플레이 트리로 묶습니다. 또한, `access`가 호출되기 전 그 루트의 스플레이 트리 안에 포함된 노드 중, `x`와 가장 가까운 것을 반환합니다.
- `link(x, y)`는 `y`를 `x`의 부모로 둡니다.
  - x의 부모가 이미 있으면 RTE입니다.
  - y가 x의 자손이면 UB입니다.
- `cut(x)`는 `x`와 `x`의 부모 사이 연결을 제거합니다.
  - x의 부모가 없으면 RTE입니다.
- `path(x, y)`는 **루트를 `x`로 바꾸고**, `x`에서 `y`로 가는 경로를 나타내는 노드를 반환합니다.
- `path_update(x, y, v)`는 `path(x, y)`에 lazy 값 `v`를 반영합니다.
- `lca(x, y)`는 `x`와 `y`의 LCA에 해당하는 노드를 반환합니다.
  - x와 y가 다른 전역 트리에 있으면 UB입니다.
- `root(x)`는 `x`의 전역 트리의 루트 노드를 반환합니다.
- `is_root(x)`는 `x`가 자신의 전역 트리의 루트 노드이면 true, 아니면 false를 반환합니다.
- `parent(x)`는 `x`의 전역 트리 상에서 자신의 부모 노드를 반환합니다.
  - 부모가 없으면 RTE입니다.
- `depth(x)`는 `x`의 전역 트리 상에서 자신의 깊이를 반환합니다. 루트의 깊이는 0입니다.
- `reroot(x)`는 루트를 `x`로 바꿉니다.
- `connect(x, y)`는 **루트를 `x`로 바꾸고**, `x`와 `y`를 간선으로 연결합니다.
- `disconnect(x, y)`는 **루트를 `x`로 바꾸고**, `x`와 `y` 사이 간선을 제거합니다.
  - 간선이 없으면 RTE입니다.
- `connected(x, y)`는 `x`와 `y`가 같은 전역 트리 상에 있으면 true, 아니면 false를 반환합니다.
- `access`부터 `connected`까지 모두, `x`와 `y`에 노드 대신 노드의 번호를 줄 수 있습니다. 이 경우 `lca`, `root`, `parent`는 노드의 번호를 반환하고, 나머지는 위에 명시한 것과 같습니다.

# `Snode`
## Declaration
- 사용자는 다음 정의를 수정해야 합니다. **뒤집는 연산은 링크/컷 트리에서 필수이기 때문에, `lazy`가 아닌 `doflip`으로 변수를 따로 만들어 놓았습니다. 따라서 `slazy_t`에 이 정보가 또 있으면 안 됩니다.**
  - `scont_t`: 노드의 내용물을 나타내는 타입.
  - `snode_t`: 서브트리의 값을 나타내는 타입.
  - `leaf_val(c)`: 노드의 자손이 없고, 내용물이 `c`일 때, 이를 서브트리 값으로 바꾸어 반환하는 함수.
  - `combine(a, b)`: 서브트리 값 `a`와 `b`를 합친 새 서브트리 값을 반환하는 함수.
  - `slazy_t`: 노드의 lazy 값을 나타내는 타입.
  - `LID`: lazy 업데이트가 없음을 의미하는 lazy 값. 노드의 lazy 값이 `LID`와 같을 경우 아래 `unlazy` 함수는 호출되지 않습니다.
  - `combine_lazy(a, b)`: 노드의 lazy 값이 `a`이고, 여기에 `b`를 반영했을 때, 새 lazy 값을 반환하는 함수.
  - `unlazy()`: 노드의 lazy 값으로부터 내용물 및 서브트리 값을 갱신하는 함수.
  - `undoflip()`: 노드의 내용물 및 서브트리 값을 뒤집는 함수.
- 사용자는 `Snode`를 선언하면 안 됩니다. `Snode`는 `LinkCut` 내부에서만 사용됩니다.

## Fields
- `content`는 노드의 내용물입니다.
- `no`는 노드의 번호입니다.
- `val`은 노드를 루트로 하는 서브트리의 값입니다.
- `cnt`는 노드를 루트로 하는 서브트리의 크기입니다.

## Methods
- `lazy_add(v)`는 노드에 lazy 값 `v`를 반영합니다.

# TODO
- `Snode`에서 사용자가 정의해야 되는 부분만 따로 빼서 별도로 정의하도록 바꾸기
- `LinkCut`에 `connect_weighted`, `disconnect_weighted` 추가하기

# 참고 자료
- 튜토리얼: [Link Cut Tree](https://imeimi.tistory.com/27?category=256657) by imeimi
- 구현: [Link Cut Tree implementation](https://codeforces.com/blog/entry/75885) by bicsi
- 구현: [LinkCutTree.cpp](https://github.com/justiceHui/AlgorithmImplement/blob/master/DataStructure/LinkCutTree.cpp) by jhnah917

# 테스트 문제
- [BOJ 트리와 쿼리 11](https://www.acmicpc.net/problem/13539) link, cut, LCA
- [BOJ 트리와 쿼리 12](https://www.acmicpc.net/problem/16912) connect, disconnect, connected
- [LC Dynamic Tree Vertex Add Path Sum](https://judge.yosupo.jp/problem/dynamic_tree_vertex_add_path_sum) connect, disconnect, path query
- [LC Dynamic Tree Vertex Set Path Composite](https://judge.yosupo.jp/problem/dynamic_tree_vertex_set_path_composite) connect, disconnect, path query
- [DMOJ Dynamic Tree Test (Easy)](https://dmoj.ca/problem/ds5easy) reroot, connect, disconnect, path query, lca

아래는 LC Dynamic Tree Vertex Set Path Composite에서의 사용 예시입니다. `Linear`는 [linear function](https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/_doc/math_linear_function.md), `modint`는 [modint](https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/_doc/math_modint.md)를 참조하세요.
```cpp
struct Snode{
	typedef Linear<modint> scont_t; // element
	typedef pair<Linear<modint>, Linear<modint>> snode_t;
	snode_t leaf_val(scont_t c){
		return {c, c};
	}
	// a left, b right
	snode_t combine(snode_t a, snode_t b){
		auto [a1, a2] = a; auto [b1, b2] = b;
		return {composite(b1, a1), composite(a2, b2)};
	}

	typedef pair<int, int> slazy_t;
	const slazy_t LID = {-1, -1};
	// apply a <- b
	slazy_t combine_lazy(slazy_t a, slazy_t b){
		return b;
	}
	void unlazy(){
		content = Linear<modint>(lazy.first, lazy.second);
	}
	void undoflip(){
		val = {val.second, val.first};
	}
	////////////////////////////////////////////////////////////
//(skipped...)
};

//(skipped...)

int main(){OJize();
	int n, Q; cin>>n>>Q;
	vector<Linear<modint>> arr(n);
	for(int i=0; i<n; i++) cin>>arr[i];
	LinkCut<Snode> LCT(arr);
	for(int i=0; i<n-1; i++){
		int x, y; cin>>x>>y;
		LCT.connect(x, y);
	}

	while(Q--){
		int qty; cin>>qty;
		if(qty == 0){
			int a, b;
			cin>>a>>b, LCT.disconnect(a, b);
			cin>>a>>b, LCT.connect(a, b);
		}
		else if(qty == 1){
			int v, a, b; cin>>v>>a>>b;
			LCT.path_update(v, v, {a, b});
		}
		else{
			int a, b, x; cin>>a>>b>>x;
			cout << LCT.path(a, b)->val.first(x) << '\n';
		}
	}
} 
```