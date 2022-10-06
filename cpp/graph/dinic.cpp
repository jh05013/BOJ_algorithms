typedef pair<int,int> EdgeIndex;
template <typename T>
struct Dinic{
	struct edge{
		int source, target; T res, orig; int revid;
		T used(){return orig-res;}
	};
	int n;
	vector<vector<edge>> adj; vector<int> dis, pnt;
	T INF;
	Dinic(int N, T INFTY): n{N}, adj(n+1), dis(n+1), pnt(n+1), INF(INFTY) {}
	EdgeIndex connect(int s, int e, T cap){
		assert(0 <= s && s <= n && 0 <= e && e <= n);
		adj[s].push_back({s, e, cap, cap, sz(adj[e])});
		adj[e].push_back({e, s, 0, 0,     sz(adj[s])-1});
		return {s, sz(adj[s])-1};
	}
	edge& operator[](EdgeIndex eidx){return adj[eidx.first][eidx.second];}

	bool bfs(int src, int sink){
		fill(entire(dis), 0), fill(entire(pnt), 0);
		queue<int> Q({src}); dis[src] = 1;
		while(!Q.empty()){
			int x = Q.front(); Q.pop();
			for(auto &e: adj[x]) if(e.res > 0 && !dis[e.target])
				dis[e.target] = dis[x]+1, Q.push(e.target);
		}
		return dis[sink] > 0;
	}
	T dfs(int x, int sink, T f){
		if(x == sink) return f;
		for(; pnt[x] < sz(adj[x]); pnt[x]++){
			edge e = adj[x][pnt[x]];
			if(e.res > 0 && dis[e.target] == dis[x]+1){
				T w = dfs(e.target, sink, min(f, e.res));
				if(!w) continue;
				adj[x][pnt[x]].res-= w, adj[e.target][e.revid].res+= w;
				return w;
			}
		}
		return 0;
	}

	T send(int src, int sink){
		T ret = 0;
		while(bfs(src, sink)){
			T r;
			while((r = dfs(src, sink, INF))) ret+= r;
		}
		return ret;
	}
};
