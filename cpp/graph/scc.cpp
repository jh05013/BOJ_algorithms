struct SCC{
	int n; vector<vector<int>> adj;
	int sccnt = 0; // number of sccs
	vector<int> scx; // idx (1-) of SCC for each vertex
	vector<vector<int>> sccs; // SCC, starts from [1]
	vector<vector<int>> dag; // graph of sccs
	vector<int> loopcnt; // number of loops for each scc

	SCC(int N): n(N), adj(N), scx(N, -1) {}
	void connect(int a, int b){
		assert(0 <= a && a < n && 0 <= b && b < n);
		adj[a].push_back(b);
	}
	void input(int m, int base=0){
		int a,b; for(int i=0;i<m;i++){cin>>a>>b; connect(a-base,b-base);}
	}
	void init(){
		int cnt = 0;
		vector<int> up(n, -1), visit(n, -1), stk;

		function<void(int)> dfs;
		dfs = [&](int v){
			up[v] = visit[v] = cnt++;
			stk.push_back(v);
			for(int nxt: adj[v]){
				if(visit[nxt] == -1) dfs(nxt), up[v] = min(up[v], up[nxt]);
				else if(scx[nxt] == -1) up[v] = min(up[v], visit[nxt]);
			}
			if(up[v] == visit[v]){
				int t = -1;
				while(!stk.empty() && t != v){
					t = stk.back(); stk.pop_back();
					scx[t] = sccnt;
				}
				sccnt++;
			}
		};
		for(int i=0; i<n; i++) if(visit[i] == -1) dfs(i);
		for(int i=0; i<n; i++) scx[i] = sccnt-scx[i]-1;

		sccs.resize(sccnt);
		for(int i=0; i<n; i++) sccs[scx[i]].push_back(i);

		dag.resize(sccnt); loopcnt.resize(sccnt);
		for(int v=0; v<n; v++) for(int u: adj[v]){
			if(scx[u] != scx[v]) dag[scx[v]].push_back(scx[u]);
			else loopcnt[scx[v]]++;
		}
	}
};