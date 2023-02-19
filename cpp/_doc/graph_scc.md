https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/graph/scc.cpp

SCC입니다.

# 선언
- `SCC(int n)`는 정점 `n`개의 그래프 `G`를 선언합니다.
  - **0-indexed**입니다.

# 그래프 만들기
- `connect(a, b)`는 `a`에서 `b`로 가는 간선을 긋습니다.
- `input(m, base)`는 `m`개의 간선을 표준 입출력으로 받습니다. `base`의 기본값은 0이고, 입력이 1-based로 들어올 경우 `base`를 1로 두면 됩니다.

# SCC 구하기
`input()`을 호출하지 않았다면, 먼저 `init()`을 호출해야 합니다.

`init()`을 호출한 뒤에는,
- `scx[v]`는 정점 `v`의 SCC 번호입니다.
  - 모든 간선 `a -> b`에 대해, `scx[a] <= scx[b]`가 성립합니다.
- `sccs[i]`는 SCC 번호가 `i`인 모든 정점의 vector이고, 정점 번호는 오름차순으로 들어있습니다.
- `dag`는 같은 SCC의 정점들을 하나로 묶었을 때 나타나는 그래프입니다.
- `loopcnt[i]`는 같은 SCC의 정점들을 하나로 묶었을 때 SCC `i`에 있는 루프의 개수입니다.

# 테스트 문제
- [BOJ 2150 Strongly Connected Component](https://www.acmicpc.net/problem/2150)
- [LC Strongly Connected Components](https://judge.yosupo.jp/problem/scc)
- [BOJ 26157 즉흥 여행 (Hard)](https://www.acmicpc.net/problem/26157)

다음은 LC Strongly Connected Components에서의 사용 예시입니다. [채점 결과](https://judge.yosupo.jp/submission/126633)

```cpp
int main(){OJize();
	int n, m; cin>>n>>m;
	SCC G(n); G.input(m);
	cout << G.sccnt << '\n';
	for(auto &V: G.sccs){
		cout << V.size() << ' ';
		for(int x: V) cout << x << ' ';
		cout << '\n';
	}
}
```
