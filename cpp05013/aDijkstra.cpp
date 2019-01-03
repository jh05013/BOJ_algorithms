// if you want to use ll, remember to change 0x3f3f3f3f!!
const int INF = 0x3f3f3f3f;
template <typename T>
struct WGraph{
    int n; vector<vector<pair<int,T>>> adj;
    WGraph(int n): n{n}, adj(n+1) {}
    void connect(int a, int b, T c){adj[a].push_back({b,c});}
    void input(int m){
        int a,b,c;
        for(int i=0;i<m;i++){cin>>a>>b>>c; connect(a,b,c);}
    }

    vector<T> dijkstra(int v){
        set<pair<T,int>> S; S.insert(make_pair(0,v));
        vector<T> dist(n+1, INF); dist[v] = 0;
        while(!S.empty()){
            int v = (*S.begin()).second, u; T c; S.erase(S.begin());
            for(auto& uc:adj[v]){
                tie(u,c) = uc;
                if(dist[u] <= dist[v]+c) continue;
                if(dist[u] != INF) S.erase(S.find({dist[u],u}));
                dist[u] = dist[v]+c; S.insert({dist[u],u});
            }
        }
        return dist;
    }
};