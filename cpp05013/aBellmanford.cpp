// any-indexed

const int INF = 0x3f3f3f3f;
vector<int> bellmanFord(int n, vector<tiii> &edge, int source){
    vector<int> dist(n+1, INF); dist[source] = 0; int u,v,c;
    for(int i=0; i<n-1; i++){
        for(tiii uvc: edge){
            tie(u,v,c) = uvc;
            dist[v] = min(dist[v], dist[u]+c);
        }
    }
    for(tiii uvc: edge){
        tie(u,v,c) = uvc;
        if(dist[u]+c < dist[v]) cout << -1, exit(0);
    }
    return dist;
}