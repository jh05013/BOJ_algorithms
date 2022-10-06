typedef pair<int,int> EdgeIndex;
template <typename T>
struct MCMF {
	struct edge{
		int source, target; T cost, res, orig; int revid;
		T used(){return orig-res;}
	};
	int n; vector<vector<edge>> adj;
	T INF;
	MCMF(int N, T INFTY): n(N), adj(n+1), INF(INFTY) {}

	EdgeIndex connect(int s, int e, T cap, T cost){
		assert(0 <= s && s <= n && 0 <= e && e <= n);
		assert(s != e);
		adj[s].push_back(edge{s, e, cost, cap, cap, sz(adj[e])  });
		adj[e].push_back(edge{e, s, -cost, 0, 0,    sz(adj[s])-1});
		return {s, sz(adj[s])-1};
	}
	edge& operator[](EdgeIndex eidx){return adj[eidx.first][eidx.second];}
	// flow, cost
	pair<T,T> aug(int s, int t, T lim){
		vector<pair<T,T>> dist(n+1, {INF, 0});
		vector<int> from(n+1, -1), A(n+1);
		A[s] = 1; dist[s] = {0, INF};
		queue<int> Q; Q.push(s);
		while(!Q.empty()){
			int v = Q.front(); A[v] = 0; Q.pop();
			for(edge &e: adj[v]){
				if(!e.res) continue;
				int next = e.target; T ncost = dist[v].first + e.cost;
				T nflow = min(dist[v].second, e.res);
				if(dist[next].first <= ncost) continue;
				dist[next] = {ncost, nflow};
				from[next] = e.revid;
				if(!A[next]) A[next] = 1, Q.push(next);
			}
		}
		int p = t; T pcost = dist[p].first, flow = dist[p].second;
		if(!flow || (lim <= 0 && pcost >= 0)) return {0, 0};
		if(lim > 0) flow = min(flow, lim);
		while(from[p] != -1){
			int ne = from[p];
			int np = adj[p][ne].target, fe = adj[p][ne].revid;
			adj[p][ne].res+= flow, adj[np][fe].res-= flow;
			p = np;
		}
		return {flow, pcost*flow};
	}
	// flow, cost
	pair<T,T> send(int s, int t){
		T cost = 0, flow = 0;
		while(1){
			auto [F, C] = aug(s, t, INF - flow);
			if(F <= 0) break;
			flow+= F, cost+= C;
		}
		return {flow, cost};
	}
};
