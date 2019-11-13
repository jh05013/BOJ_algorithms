// Thanks to koosaga for code
struct Blossom{
    int n, t;
    vector<vector<int>> adj;
    vector<int> orig, par, vis, match, aux;
    queue<int> Q;
    Blossom(int n): n{n}, t{0}, adj(n+1), orig(n+1), par(n+1),
        vis(n+1), match(n+1), aux(n+1) {}
    void connect(int a, int b){
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    void augment(int u, int v){
        int pv = v, nv;
        do{
            pv = par[v], nv = match[pv];
            match[v] = pv, match[pv] = v;
            v = nv;
        } while(u != pv);
    }
    int lca(int v, int w){
        ++t;
        while(1){
            if(v){
                if(aux[v] == t) return v;
                aux[v] = t, v = orig[par[match[v]]];
            }
            swap(v, w);
        }
    }
    void blossom(int v, int w, int a){
        while(orig[v] != a){
            par[v] = w, w = match[v];
            if(vis[w] == 1) Q.push(w), vis[w] = 0;
            orig[v] = orig[w] = a;
            v = par[w];
        }
    }
    bool bfs(int u){
        fill(entire(vis), -1), iota(entire(orig), 0);
        Q = queue<int>(); Q.push(u), vis[u] = 0;
        while(!Q.empty()){
            int v = Q.front(); Q.pop();
            for(int x: adj[v]){
                if(vis[x] == -1){
                    par[x] = v, vis[x] = 1;
                    if(!match[x]) return augment(u, x), true;
                    Q.push(match[x]); vis[match[x]] = 0;
                }
                else if(vis[x] == 0 && orig[v] != orig[x]){
                    int a = lca(orig[v], orig[x]);
                    blossom(x, v, a), blossom(v, x, a);
                }
            }
        }
        return false;
    }

    int solve(){
        int ans = 0;
        for(int x=1; x<=n; x++) if(!match[x]){
            for(int y: adj[x]) if(!match[y]){
                match[x] = y, match[y] = x;
                ++ans; break;
            }
        }
        for(int i=1; i<=n; i++) if(!match[i] && bfs(i)) ++ans;
        return ans;
    }
};