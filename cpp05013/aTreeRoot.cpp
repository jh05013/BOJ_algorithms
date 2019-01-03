vector<vector<int>> setroot(vector<vector<int>>& adj, int r){
    vector<bool> visit(adj.size()); visit[r] = 1;
    vector<vector<int>> tadj(adj.size());
    queue<int> Q; Q.push(r);
    while(!Q.empty()){
        int v = Q.front(); Q.pop();
        for(int u: adj[v]){
            if(visit[u]) continue;
            visit[u] = true; Q.push(u);
            tadj[v].push_back(u);
        }
    }
    return tadj;
}