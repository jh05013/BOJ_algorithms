// 1-indexed
const int INF = 0x3f3f3f3f;
struct Hopk{
    int n, m; vector<vector<int>> adj; vector<int> pu, pv, dist;
    Hopk(int n, int m): n(n), m(m), adj(n+1), pu(n+1), pv(m+1), dist(n+1, -1) {}
    void connect(int a, int b){adj[a].push_back(b);}
    bool bfs(){
        queue<int> Q;
        for(int u=1; u<=n; u++){
            if(!pu[u]) dist[u] = 0, Q.push(u);
            else dist[u] = INF;
        }
        dist[0] = INF;
        while(!Q.empty()){
            int u = Q.front(); Q.pop();
            if(dist[u] >= dist[0]) continue;
            for(int v: adj[u]) if(dist[pv[v]] == INF){
                dist[pv[v]] = dist[u] + 1;
                Q.push(pv[v]);
            }
        }
        return dist[0] != INF;
    }
    bool dfs(int u){
        if(!u) return true;
        for(int v: adj[u]) if(dist[pv[v]] == dist[u] + 1 && dfs(pv[v])){
            pv[v] = u, pu[u] = v;
            return true;
        }
        dist[u] = INF;
        return false;
    }
    int send(){
        int match = 0;
        while(bfs()) for(int u=1; u<=n; u++) if(!pu[u]) match+= dfs(u);
        return match;
    }
};