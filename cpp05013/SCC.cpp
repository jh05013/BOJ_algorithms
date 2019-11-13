struct Graph{
    int n, cnt, sccnt; vector<vector<int>> adj;
    vector<int> up, visit, scx, stk;
    Graph(int n): n(n), adj(n+1), up(n+1), visit(n+1), scx(n+1) {}
    void connect(int a, int b){adj[a].push_back(b);}
    void input(int m){
        int a,b;
        for(int i=0;i<m;i++){cin>>a>>b; connect(a,b);}
    }
    void dfs(int v){
        up[v] = visit[v] = ++cnt;
        stk.push_back(v);
        for(int nxt: adj[v]){
            if(!visit[nxt]) dfs(nxt), up[v] = min(up[v], up[nxt]);
            else if(!scx[nxt]) up[v] = min(up[v], visit[nxt]);
        }
        if(up[v] == visit[v]){
            ++sccnt; int t = -1;
            while(!stk.empty() && t != v){
                t = stk.back(); stk.pop_back();
                scx[t] = sccnt;
            }
        }
    }
    void getscc(){
        cnt = sccnt = 0;
        for(int i=1; i<=n; i++) if(!visit[i]) dfs(i);
    }
    vector<vector<int>> scc(){
        getscc();
        vector<vector<int>> res(sccnt);
        for(int i=1; i<=n; i++) res[scx[i]-1].push_back(i);
        return res;
    }
    vector<vector<int>> dag(){
        getscc();
        vector<vector<int>> res(*max_element(entire(scx))+1);
        for(int v=1; v<=n; v++){
            for(int u: adj[v]) if(scx[u] != scx[v]) res[scx[v]].push_back(scx[u]);
        }
        return res;
    }
    vector<vector<int>> rdag(){
        getscc();
        vector<vector<int>> res(*max_element(entire(scx))+1);
        for(int v=1; v<=n; v++){
            for(int u: adj[v]) if(scx[u] != scx[v]) res[scx[u]].push_back(scx[v]);
        }
        return res;
    }
};