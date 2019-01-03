// any-indexed
struct Dinic {
    struct edge {int next; size_t inv; int res;};
    int n; vector<vector<edge>> adj; vector<int> l, start;
    Dinic(int n): n(n), adj(n+1), l(n+1), start(n+1) {}
    void connect(int s, int e, int cap, int rev = 0){
        adj[s].emplace_back(edge{e, adj[e].size(), cap});
        adj[e].emplace_back(edge{s, adj[s].size(), rev});
    }
    bool bfs(int source, int sink){
        fill(entire(l), 0); l[source] = 1;
        queue<int> Q; Q.push(source);
        while(!Q.empty() && !l[sink]){
            int v = Q.front(); Q.pop();
            for(edge& e: adj[v]){
                if(l[e.next] || !e.res) continue;
                l[e.next] = l[v] + 1;
                Q.push(e.next);
            }
        }
        return l[sink] != 0;
    }
    int block(int v, int sink, int flow){
        if(v == sink) return flow;
        for(size_t i=start[v]; i<adj[v].size(); i++){
            edge& e = adj[v][i]; start[v]++;
            if(!e.res || l[e.next] != l[v] + 1) continue;
            if(int res = block(e.next, sink, min(e.res, flow))){
                e.res-= res;
                adj[e.next][e.inv].res+= res;
                return res;
            }
        }
        return 0;
    }
    int send(int source, int sink){
        int ans = 0;
        while(bfs(source, sink)){
            fill(entire(start), 0);
            while(int flow = block(source, sink, 2147483647)) ans+= flow;
        }
        return ans;
    }
};