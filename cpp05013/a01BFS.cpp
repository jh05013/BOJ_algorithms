typedef pair<int, int> pii;
struct W01graph{
    int n; vector<vector<pii>> adj;
    W01graph(int n): n{n}, adj(n+1) {}
    void connect(int a, int b, bool c){adj[a].push_back(pii(b,c));}
    
    vector<int> bfs(int v){
        deque<int> Q; Q.push_front(v);
        vector<int> dist(n+1, 2*n); dist[v] = 0;
        while(!Q.empty()){
            int v = Q.front(); Q.pop_front();
            for(pii& uc: adj[v]){
                int u = uc.first, c = uc.second;
                if(dist[u] <= dist[v] + c) continue;
                dist[u] = dist[v] + c;
                if(c == 0) Q.push_front(u);
                else Q.push_back(u);
            }
        }
        return dist;
    }
};

bool ingrid(int i, int j, int n, int m){return 0<=i && i<n && 0<=j && j<m;}
int di[4] = {-1,0,1,0};
int dj[4] = {0,-1,0,1};