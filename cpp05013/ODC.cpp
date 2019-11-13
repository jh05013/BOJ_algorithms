// Offline dynamic connectivity
// probably 1-indexed, idk
// solve() saves the answer to the i-th query to answer[i]
//     provided that the i-th query is a question

struct DisjointHist{
    vector<int> par, sz;
    vector<pair<int, int>> history;
    DisjointHist(int n): par(n+1), sz(n+1, 1) {iota(entire(par), 0);}

    void un(int x, int y){
        x = fd(x), y = fd(y);
        if(x == y) return;
        if(sz[x] < sz[y]) swap(x, y);
        history.push_back({x, y});
        par[y] = x, sz[x]+= sz[y];
    }
    int fd(int x){return par[x]!=x? fd(par[x]) : x;}
    void rollback(){
        auto [x,y] = history.back(); history.pop_back();
        par[x] = x, par[y] = y, sz[x]-= sz[y];
    }
};

struct ODC{
    int n, Q, time = 0;
    DisjointHist DS;
    vector<map<int,int>> adj; // [u][v] -> addtime
    vector<int> end; // ending time of edge added at i
    vector<int> qtype; // 1 add 2 remove 3 question
    vector<pair<int,int>> quest; // pair of vertices at query i
    vector<bool> answer; // answer to the questions
    ODC(int n, int Q): n{n}, Q{Q}, DS(n), adj(n+1),
        end(Q), qtype(Q), quest(Q), answer(Q) {}

    void add(int x, int y){
        if(x > y) swap(x, y);
        quest[time] = {x,y}, qtype[time] = 1, end[time] = Q-1;
        adj[x][y] = time++;
    }
    void rem(int x, int y){
        if(x > y) swap(x, y);
        quest[time] = {x,y}, qtype[time] = 2;
        end[adj[x][y]] = time++;
    }
    void query(int x, int y){
        if(x > y) swap(x, y);
        quest[time] = {x, y}, qtype[time++] = 3;
    }

    void solve(){
        vector<int> E;
        for(int i=0; i<Q; i++) if(qtype[i] == 1) E.push_back(i);
        solve(0, Q-1, E);
    };
    void solve(int s, int e, vector<int> &E){
        if(s > e) return;
        int startnum = DS.history.size();

        int mid = (s+e)/2;
        vector<int> E1, E2;
        for(int i: E){
            auto [x,y] = quest[i];
            if(i <= s && e <= end[i]) DS.un(x, y);
            else{
                if(!(end[i] < s || i > mid)) E1.push_back(i);
                if(!(end[i] < mid+1 || i > e)) E2.push_back(i);
            }
        }

        if(s == e){
            auto [x,y] = quest[s];
            if(qtype[s] == 3) answer[s] = (DS.fd(x) == DS.fd(y));
        }
        else solve(s, mid, E1), solve(mid+1, e, E2);
        while(DS.history.size() != startnum) DS.rollback();
    }
};