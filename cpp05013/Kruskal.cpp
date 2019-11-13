struct disjointSet{
    vector<int> par;
    disjointSet(int n): par{vector<int>(n)} {iota(entire(par), 0);}
    void un(int x, int y){par[fd(x)] = fd(y);} // yr becomes parent
    int fd(int x){return par[x]!=x? (par[x]=fd(par[x])) : x;}
};

typedef tuple<int, int, int> tiii;
int kruskal(int n, vector<tiii> &edge, bool sorted){
    if(!sorted) sort(entire(edge));
    disjointSet DS(n+1);
    int cost = 0;
    for(tiii cab: edge){
        int a,b,c; tie(c,a,b) = cab;
        if(DS.fd(a) != DS.fd(b)) cost+= c, DS.un(a, b);
    }
    return cost;
}