// No union by rank
struct DisjointSet{
    vector<int> par;
    DisjointSet(int n): par(n) {iota(entire(par), 0);}
    void un(int x, int y){par[fd(x)] = fd(y);} // yr becomes parent
    int fd(int x){return par[x]!=x? (par[x]=fd(par[x])):x;}
};

// Expanded union/findr to give space for additional features
struct DisjointSet{
    vector<int> par;
    DisjointSet(int n): par(n) {iota(entire(par), 0);}
    void un(int x, int y){ // yr becomes parent
        int xr = findr(x), yr = findr(y);
        if(xr == yr) return;
        par[xr] = yr;
    }
    int fd(int x){
        if(par[x] != x) par[x] = findr(par[x]);
        return par[x];
    }
};