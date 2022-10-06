https://github.com/jh05013/BOJ_algorithms/blob/master/cpp/graph/dinic.cpp

최대 유량입니다.

# 선언
- `Dinic<T>(int n, T INFTY)`는 정점 `n`개의 플로우 그래프 `G`를 선언합니다.
  - `T`는 간선의 용량의 타입입니다.
  - `INFTY`는 무한대 값입니다.

# 그래프 만들기
- `connect(s, e, cap)`은 `s`에서 `e`로 가는 용량 `cap`의 간선을 긋습니다.
  - 추가로, 그 간선을 찾는 데 사용되는 `EdgeIndex ei`를 반환합니다. `G[ei]`를 사용하면 됩니다. `G[ei].source, G[ei].target, G[ei].orig`는 각각 `s, e, cap`입니다.

# 유량 구하기
- `send(s, t)`는 `s`에서 `t`로 가는 최대 유량을 찾아 `{유량, 비용}` pair를 반환합니다.
  - `send`를 여러 번 호출하지 마세요.
- 그 후, 특정 간선의 `EdgeIndex`가 `ei`일 때, `G[ei].used()`는 그 간선에서 사용된 유량을 반환합니다.

# 테스트 문제
- [BOJ 15892 사탕 줍는 로봇](https://www.acmicpc.net/problem/15892)
- [LibreOJ 101 最大流](https://loj.ac/p/101)
- [BOJ 11377 열혈강호 3](https://acmicpc.net/problem/11408) bipartite matching
- [BOJ 11378 열혈강호 4](https://acmicpc.net/problem/11409) bipartite matching
- [BOJ 17412 도시 왕복하기 1](https://www.acmicpc.net/problem/17412)

다음은 LibreOJ 101에서의 사용 예시입니다. [채점 결과](https://loj.ac/s/1597352)

```cpp
int main(){OJize();
	int n,m,s,t; cin>>n>>m>>s>>t;
	Dinic<ll> D(n+1, 0x3f3f3f3f4f3f3f3f);
	for (int i=0; i<m; i++){
		int a, b; ll c; cin>>a>>b>>c;
		D.connect(a, b, c);
	}
	cout << D.send(s, t);
}
```
