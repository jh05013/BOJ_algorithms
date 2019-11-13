struct Graph{
    int n; vector<vector<int>> adj;
    Graph(int n): n{n}, adj(n+1) {}
    void connect(int a, int b){adj[a].push_back(b);}
    void input(int m){
        int a,b;
        for(int i=0;i<m;i++){cin>>a>>b; connect(a,b);}
    }
    vector<int> toposort(){
        vector<int> indg(n+1), L;
        queue<int> Q;
        for(int i=1; i<=n; i++) for(int j: adj[i]) indg[j]++;
        for(int i=1; i<=n; i++) if(!indg[i]) Q.push(i);
        for(int i=0; i<n; i++){
            if(Q.empty()) assert(0); // Change this if you need something
            int p = Q.front(); Q.pop();
            L.push_back(p);
            for(int j: adj[p]) if (!--indg[j]) Q.push(j);
        }
        return L;
    }
};