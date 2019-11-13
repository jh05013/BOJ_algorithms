// 0/1-indexed
struct ETT{
    int n, i = 0; vector<vector<int>> adj;
    vector<int> seq, start, end;
    ETT(int n): n{n}, adj(n+1), seq(2*n), start(n+1, -1), end(n+1, -1) {}
    void connect(int a, int b){
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    void dfs(int v){
        start[v] = i, seq[i++] = v;
        for(int u: adj[v]) if(start[u] == -1) dfs(u);
        end[v] = i-1;
    }
};