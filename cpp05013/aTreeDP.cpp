// 1-indexed
struct Tree{
    int n; vector<int> ord; vector<vector<int>> adj;
    Tree(int n): n{n}, ord(n+1), adj(n+1) {}
    void connect(int a, int b){adj[a].push_back(b); adj[b].push_back(a);}
    void input(){for(int i=0; i<n-1; i++){int a, b; cin>>a>>b; connect(a,b);}}
    void root(int r){
        vector<vector<int>> tadj(n+1); vector<bool> vis(n+1); queue<int> Q;
        Q.push(r); vis[r] = true;
        while(!Q.empty()){
            int v = Q.front(); Q.pop();
            ord.push_back(v);
            for(int u: adj[v]) if(!vis[u]){
                vis[u] = true; Q.push(u); tadj[v].push_back(u);
            }
        }
        adj.clear(); swap(adj, tadj);
        reverse(entire(ord));
    }
};