// Stoer-Wagner algorithm
// 0-indexed

struct Mincut{
    int n; vector<vector<int>> graph;
    Mincut(int n): n{n}, graph(n, vector<int>(n)) {}
    void connect(int a, int b, int w){if(a != b) graph[a][b]+= w, graph[b][a]+= w;}
    
    pair<int, pair<int, int>> stmin(vector<int> &active){
        vector<int> key(n), v(n);
        int s = -1, t = -1;
        for(size_t i=0; i<active.size(); i++){
            int maxv = -1, cur = -1;
            for(auto j: active) if(!v[j] && maxv < key[j]) maxv = key[j], cur = j;
            t = s, s = cur; v[cur] = 1;
            for(auto j: active) key[j] += graph[cur][j];
        }
        return make_pair(key[s], make_pair(s, t));
    }

    vector<int> cut;
    int solve(){
        int res = numeric_limits<int>::max();
        vector<vector<int>> grps; vector<int> active;
        cut.resize(n);
        for(int i=0; i<n; i++) grps.emplace_back(1, i);
        for(int i=0; i<n; i++) active.push_back(i);
        while(active.size() >= 2){
            auto stcut = stmin(active);
            if(stcut.first < res){
                res = stcut.first;
                fill(entire(cut), 0);
                for(auto v: grps[stcut.second.first]) cut[v] = 1;
            }
            int s, t; tie(s, t) = stcut.second;
            if(grps[s].size() < grps[t].size()) swap(s, t);
            active.erase(find(entire(active), t));
            grps[s].insert(grps[s].end(), entire(grps[t]));
            for(int i=0; i<n; i++) graph[i][s]+= graph[i][t], graph[i][t] = 0;
            for(int i=0; i<n; i++) graph[s][i]+= graph[t][i], graph[t][i] = 0;
            graph[s][s] = 0;
        }
        return res;
    }
};