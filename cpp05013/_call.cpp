#include <bits/stdc++.h>
#define dbgv(v) {for(auto x:v)cout<<x<<' ';cout<<'\n';}
#define entire(v) v.begin(),v.end()
using namespace std;
void OJize(){
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    #ifdef jh
    freopen("input.txt", "r", stdin);
    #endif
}

typedef pair<int, int> pii;
template <typename T>
struct WGraph{
    int n; vector<vector<pair<int,T>>> adj;
    WGraph(int n): n{n}, adj{vector<vector<pair<int,T>>>(n+1)} {}
    void connect(int a, int b, T c){adj[a].push_back(make_pair(b,c));}
    void input(int m){
        int a,b,c;
        for(int i=0;i<m;i++){cin>>a>>b>>c; connect(a,b,c);}
    }

    vector<T> dijkstra(int v){
        set<pair<T, int>> S; S.insert(make_pair(0,v));
        vector<T> dist(n+1, 0x3f3f3f); dist[v] = 0;
        while(!S.empty()){
            int v = (*S.begin()).second, u, c; S.erase(S.begin());
            for(auto& uc:adj[v]){
                tie(u,c) = uc;
                if(dist[u] <= dist[v]+c) continue;
                if(dist[u] != 0x3f3f3f) S.erase(S.find(make_pair(dist[u],u)));
                dist[u] = dist[v]+c; S.insert(make_pair(dist[u],u));
            }
        }
        return dist;
    }
};

bool ingrid(int i, int j, int n, int m){return 0<=i && i<n && 0<=j && j<m;}

int di[4] = {-1,0,1,0};
int dj[4] = {0,-1,0,1};
bool solve(){
    int n, m;
    if(!(cin>>n>>m)) return false;
    vector<string> grid(n);
    for(int i=0; i<n; i++) cin>>grid[i];
    for(string& s: grid) cout<<s<<'\n';
    
    WGraph<int> G(n*m);
    for(int i=0; i<n; i++) for(int j=0; j<m; j++){
        for(int d=0; d<4; d++){
            int ni = i+di[d], nj = j+dj[d];
            if(ingrid(ni,nj,n,m) && grid[ni][nj] == '.') G.connect(m*i+j, m*ni+nj, 0);
        }
        for(int exi=-3; exi<=3; exi++) for(int exj=-3; exj<=3; exj++){
            if(abs(exi) == 3 && abs(exj) == 3) continue;
            int ni = i+exi, nj = j+exj;
            if(ingrid(ni,nj,n,m)) G.connect(m*i+j, m*ni+nj, 1);
        }
    }
    
    int ans = G.dijkstra(0)[n*m-1];

    cout << ans << '\n';
    int real; cin>>real;
    cout << real << '\n';
    assert(ans == real);
    
    return true;
}

int main(){OJize();
    while(solve());
}