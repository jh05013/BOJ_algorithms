int sqrtn; // Change this to sqrt(n) in the main!
struct moquery{
    int s, e, n; // start, end, query-index
    moquery(int s, int e, int n): s(s), e(e), n(n){}
    bool operator<(const moquery& O) const{
        if(s/sqrtn != O.s/sqrtn) return (s/sqrtn < O.s/sqrtn);
        return e < O.e;
    }
};

struct Mos{
    vector<int> A;
    vector<moquery> Q;
    int ans;
    // DEFINE OTHER PROPERTIES HERE
    
    Mos(int n): A(n+1), ans(0){} // INITIALIZE OTHER PROPERTIES HERE
    void query(int a, int b){Q.push_back(moquery(a, b, Q.size()));}
    
    void first(int s, int e){
        // [s, e] is the FIRST QUERY
    }
    void add(int x){
        // x is to be ADDED
    }
    void rem(int x){
        // x is to be REMOVED
    }
    
    void process(){
        vector<ll> result(Q.size());
        sort(entire(Q));
        // Find the answers
        int s = Q[0].s, e = Q[0].e;
        first(s, e);
        result[Q[0].n] = ans;
        for(size_t i=1; i<Q.size(); i++){
            while(Q[i].s < s) add(A[--s]);
            while(e < Q[i].e) add(A[++e]);
            while(Q[i].s > s) rem(A[s++]);
            while(e > Q[i].e) rem(A[e--]);
            result[Q[i].n] = ans;
        }
        // OUTPUT
        for(auto x: result) cout<<x<<'\n';
    }
};