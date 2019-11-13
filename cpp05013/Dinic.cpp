// any-indexed
struct Dinic{
    typedef int T;
    const T INF = 0x3f3f3f3f;
    struct edge{int pos; T cap; int rev;};
    vector<vector<edge>> adj; vector<int> dis, pnt;
    Dinic(int n): adj(n+1), dis(n+1), pnt(n+1) {}
    void connect(int a, int b, T cap){
        adj[a].push_back({b, cap, (int)adj[b].size()});
        adj[b].push_back({a, 0, (int)adj[a].size()-1});
    }

    bool bfs(int src, int sink){
        fill(entire(dis), 0), fill(entire(pnt), 0);
        queue<int> Q({src}); dis[src] = 1;
        while(!Q.empty()){
            int x = Q.front(); Q.pop();
            for(auto &e: adj[x]) if(e.cap > 0 && !dis[e.pos])
                dis[e.pos] = dis[x]+1, Q.push(e.pos);
        }

        return dis[sink] > 0;
    }
    T dfs(int x, int sink, T f){
        if(x == sink) return f;
        for(; pnt[x] < (int)adj[x].size(); pnt[x]++){
            edge e = adj[x][pnt[x]];
            if(e.cap > 0 && dis[e.pos] == dis[x]+1){
                T w = dfs(e.pos, sink, min(f, e.cap));
                if(!w) continue;
                adj[x][pnt[x]].cap-= w, adj[e.pos][e.rev].cap+= w;
                return w;
            }
        }
        return 0;
    }

    T send(int src, int sink){
        T ret = 0;
        while(bfs(src, sink)){
            T r;
            while((r = dfs(src, sink, INF))) ret+= r;
        }
        return ret;
    }
};