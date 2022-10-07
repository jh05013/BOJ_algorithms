https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/graph/mcmf.cpp

MCMF입니다.

# 선언
- `MCMF<T>(int n, T INFTY)`는 정점 `n`개의 MCMF 그래프 `G`를 선언합니다.
  - `T`는 간선의 용량 및 비용의 타입입니다.
  - `INFTY`는 무한대 값입니다.

# 그래프 만들기
- `connect(s, e, cap, cost)`는 `s`에서 `e`로 가는 용량 `cap`, 비용 `cost`의 간선을 긋습니다.
  - `s != e`여야 합니다. 안 그러면 RTE입니다.
  - 추가로, 그 간선을 찾는 데 사용되는 `EdgeIndex ei`를 반환합니다. `G[ei]`를 사용하면 됩니다. `G[ei].source, G[ei].target, G[ei].cost, G[ei].orig`는 각각 `s, e, cost, cap`입니다.
- **그래프에 음수 사이클이 있으면 UB입니다.**

# 유량 구하기
- `send(s, t)`는 `s`에서 `t`로 가는 최소 비용 최대 유량을 찾아 `{유량, 비용}` pair를 반환합니다.
  - `send`를 여러 번 호출하지 마세요.
- 그 후, 특정 간선의 `EdgeIndex`가 `ei`일 때, `G[ei].used()`는 그 간선에서 사용된 유량을 반환합니다.

# 테스트 문제
- [BOJ 11408 열혈강호 5](https://acmicpc.net/problem/11408) bipartite matching
- [BOJ 11409 열혈강호 6](https://acmicpc.net/problem/11409) bipartite matching
- [LibreOJ 102 最小费用流](https://loj.ac/p/102)

다음은 LibreOJ 102에서의 사용 예시입니다. [채점 결과](https://loj.ac/s/1597372)

```cpp
int main(){OJize();
	int n, m; cin>>n>>m;
	MCMF<ll> G(n+1, 0x3f3f3f3f4f3f3f3f);
	for(int i=0; i<m; i++){
		int a, b; ll cap, cost; cin>>a>>b>>cap>>cost;
		G.connect(a, b, cap, cost);
	}
	auto [F, C] = G.send(1, n);
	cout << F << ' ' << C;
}
```
