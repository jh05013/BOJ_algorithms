// 1-indexed
template <typename T>
struct WTree{
    int n; vector<int> ord; vector<vector<pair<int,T>>> adj;
    WTree(int n): n{n}, ord(n+1), adj(n+1) {}
    void connect(int a, int b, T c){
        adj[a].push_back(make_pair(b,c)); adj[b].push_back(make_pair(a,c));
    }
    void input(){for(int i=0; i<n-1; i++){int a,b;T c;cin>>a>>b>>c; connect(a,b,c);}}
    void root(int r){
        vector<vector<pair<int,T>>> tadj(n+1); vector<bool> vis(n+1); queue<int> Q;
        Q.push(r); vis[r] = true;
        while(!Q.empty()){
            int v = Q.front(); Q.pop();
            ord.push_back(v);
            for(auto& uc: adj[v]) {
                int u = uc.first; T c = uc.second;
                if(vis[u]) continue;
                vis[u] = true; Q.push(u); tadj[v].push_back(pair<int,T>(u,c));
            }
        }
        adj.clear(); swap(adj, tadj);
        reverse(entire(ord));
    }
};