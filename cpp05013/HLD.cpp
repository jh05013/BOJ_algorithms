// HLD, any-indexed
// If the edges have values, then treat it as
// "child node has that value"
// If the nodes have values, then
// change depth[x] > depth[y] to depth[x] >= depth[y] and
// change in[]+1 to in[]

// Variables used:
// adj = bidirectional adjacency list
// tadj = tree adjacency list
// sz = size of the subtree
// par = parent of the node
// dep = depth of the node; root depth is 0
// in = in-number of the node, usable for the segment tree
// top = top node of the group containing this node

struct HLD{
    int n, t;
    vector<vector<int>> adj, tadj;
    vector<int> sz, par, dep, in, top;

    HLD(int n): n{n}, t{0}, adj(n+1), tadj(n+1), sz(n+1), par(n+1),
        dep(n+1), in(n+1), top(n+1) {}
    void connect(int a, int b){adj[a].push_back(b); adj[b].push_back(a);}

    void dfs_tree(int v, int prev=-1){
        for(int u: adj[v]){
            if(u == prev) continue;
            tadj[v].push_back(u); par[u] = v; dep[u] = dep[v]+1;
            dfs_tree(u, v);
        }
    }
    void dfs_sz(int v){
        sz[v] = 1;
        for(int &u: tadj[v]){
            dfs_sz(u); sz[v]+= sz[u];
            if(sz[u] > sz[tadj[v][0]]) swap(u, tadj[v][0]);
        }
    }
    void dfs_hld(int v){
        in[v] = t++;
        for(int u: tadj[v]) top[u] = (u==tadj[v][0]? top[v]:u), dfs_hld(u);
    }
    void init(int i=1){
        dfs_tree(i); adj.clear(); dfs_sz(i); dfs_hld(i);
    }

    // Decompose the x--y path into groups usable for ST
    vector<pair<int,int>> path(int x, int y){
        vector<pair<int,int>> ans;
        while(top[x] != top[y]){
            int xt = top[x], yt = top[y], a, b;
            if(dep[xt] > dep[yt]) ans.push_back({in[xt], in[x]}), x=par[xt];
            else ans.push_back({in[yt], in[y]}), y=par[yt];
        }
        if(dep[x] >= dep[y]) ans.push_back({in[y], in[x]});
        else if(dep[x] < dep[y]) ans.push_back({in[x], in[y]});
        return ans;
    }

    // subtree of v = [in[v] ... in[v]+sz[v]-1]
    // top of a group with v = top[v]
    // vertices in a group have consecutive in[]
};