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
    vector<moquery> Q;
    ll ans = 0;
    vector<int> arr; // or ll
    // DEFINE OTHER PROPERTIES HERE
    
    // INITIALIZE OTHER PROPERTIES BELOW
    Mos(int n): ans(0), arr(n+1){} 
    void query(int a, int b){Q.push_back(moquery(a, b, Q.size()));}

    void add(int x, bool fromend){
        // Add x from left (0) or right (1)
    }
    void rem(int x, bool fromend){
        // Remove x from left (0) or right (1)
    }
    
    void process(){
        vector<ll> result(Q.size());
        sort(entire(Q));
        // Find the answers
        int s = Q[0].s, e = Q[0].e;
        for(int i=s; i<=e; i++) add(arr[i], 1);
        result[Q[0].n] = ans;
        for(size_t i=1; i<Q.size(); i++){
            while(Q[i].s < s) add(arr[--s], 0);
            while(e < Q[i].e) add(arr[++e], 1);
            while(Q[i].s > s) rem(arr[s++], 0);
            while(e > Q[i].e) rem(arr[e--], 1);
            result[Q[i].n] = ans;
        }
        // OUTPUT
        for(auto x: result) cout<<x<<'\n';
    }
};