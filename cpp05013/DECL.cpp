typedef pair<ll,ll> pll;
// positive -> ccw; negative -> cw; 0 -> collinear
ll ccw(pll &a, pll &b, pll &c){
    auto [ax,ay] = a; auto [bx,by] = b; auto [cx,cy] = c;
    return (bx-ax)*(cy-ay) - (by-ay)*(cx-ax);
}

struct DCEL{
    int n, i=0;
    vector<pll> P, edge;
    vector<vector<pll>> adj;
    vector<int> nxt;
    DCEL(int n): n{n}, P(n+1), adj(n+1), nxt(n+1) {}

    bool comp(int a, int b, int c){
        if((P[b]<P[a]) != (P[c]<P[a])) return P[b]<P[a];
        return ccw(P[a], P[b], P[c]) > 0;
    }
    void connect(int a, int b){
        adj[a].push_back({b, 2*i}), edge.push_back({a,b});
        adj[b].push_back({a, 2*(i++)+1}), edge.push_back({b,a});
    }

    void init(){
        nxt.resize(edge.size());
        for(int i=1; i<=n; i++){
            sort(entire(adj[i]), [&,i](pll &a, pll &b)
                {return comp(i, a.first, b.first);});
            int S = adj[i].size();
            for(int j=0; j<S; j++)
                nxt[adj[i][j].second^1] = adj[i][(j+S-1)%S].second;
        }
    }

    vector<vector<int>> faces(){
        vector<vector<int>> ans;
        for(int i=0; i<edge.size(); i++) if(nxt[i] != -1){
            int x = i, temp;
            vector<int> V;
            do{
                V.push_back(edge[x].first);
                temp = nxt[x], nxt[x] = -1, x = temp;
            } while(x != i);
            ans.push_back(V);
        }
        return ans;
    }
};