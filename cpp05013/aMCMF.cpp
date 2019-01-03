struct MCMF {
    struct edge{int target, cost, res, orig; size_t revid;};
    int n; vector<vector<edge>> adj;
    MCMF(int n): n(n), adj(n+1) {}
    void connect(int s, int e, int cap, int cost){
        adj[s].emplace_back(edge{e, cost, cap, cap, adj[e].size()});
        adj[e].emplace_back(edge{s, -cost, 0, 0, adj[s].size()-1});
    }
    pii aug(int s, int e, int lim){
        vector<pii> dist(n+1, pii(2147483647, 0));
        vector<int> from(n+1, -1), A(n+1);
        A[s] = 1; dist[s] = pii(0, 2147483647);
        queue<int> Q; Q.push(s);
        while(!Q.empty()){
            int v = Q.front(); A[v] = 0; Q.pop();
            for(edge& e: adj[v]){
                if(!e.res) continue;
                int next = e.target, ncost = dist[v].first + e.cost;
                int nflow = min(dist[v].second, e.res);
                if(dist[next].first <= ncost) continue;
                dist[next] = pii(ncost, nflow);
                from[next] = e.revid;
                if(!A[next]) A[next] = 1, Q.push(next);
            }
        }
        int p = e, pcost = dist[p].first, flow = dist[p].second;
        if(!flow || (lim <= 0 && pcost >= 0)) return pii(0, 0);
        if(lim > 0) flow = min(flow, lim);
        while(from[p] != -1){
            int ne = from[p];
            int np = adj[p][ne].target, fe = adj[p][ne].revid;
            adj[p][ne].res+= flow, adj[np][fe].res-= flow;
            p = np;
        }
        return pii(pcost*flow, flow);
    }
    pii send(int s, int e, int fmin = 2147483647){
        int cost = 0, flow = 0;
        while(1){
            pii res = aug(s, e, fmin - flow);
            if(res.second <= 0) break;
            cost+= res.first, flow+= res.second;
        }
        return pii(cost, flow);
    }
};