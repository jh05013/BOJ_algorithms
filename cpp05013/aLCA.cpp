// 1-indexed

struct LCA{
    int n, k=1; vector<int> depth; vector<vector<int>> pk;
    LCA(vector<vector<int>>& adj): n{(int)adj.size()-1}{
        depth.resize(n+1);
        while(k <= n) pk.emplace_back(vector<int>(n+1)), k*= 2;
        queue<int> Q; Q.push(1); pk[0][1] = 1; depth[1] = 1;
        while(!Q.empty()){
            int p = Q.front(); Q.pop();
            for(int q: adj[p]) if(!depth[q])
                depth[q] = depth[p]+1, pk[0][q] = p, Q.push(q);
        }
        for(size_t d=1; d<pk.size(); d++){
            for(int i=1; i<=n; i++) pk[d][i]= pk[d-1][pk[d-1][i]];
        }
    }
    int kpar(int a, int k){
        int j = 0;
        for(; k; k/=2, j++) if(k%2) a = pk[j][a];
        return a;
    }
    int lca(int a, int b){
        if(depth[a] < depth[b]) swap(a, b);
        a = kpar(a, depth[a] - depth[b]);
        if(a == b) return a;
        for(int j=pk.size()-1; j>=0; j--){
            if(pk[j][a] && pk[j][a] != pk[j][b]) a = pk[j][a], b = pk[j][b];
        }
        return pk[0][a];
    }
};