// 0-indexed
struct Seglazy{
    typedef int T1; // Change this to what you need
    typedef int T2; // Change this to what you need
    T1 id = 0, initval = 0;
    T2 unused = 0;
    T1 combine(T1 a, T1 b){
        // Real value when a <-- b
    }
    T2 combineL(T2 a, T2 b){
        // Lazy value when a <-- b
    }
    void unlazy(int i, int nl, int nr){
        // Real value when its lazy is applied
    }
    
    int n; vector<T1> arr; vector<T2> lazy;
    Seglazy(int sz): n{1} {
        while(n < sz) n<<=1;
        arr.resize(n*2, initval); lazy.resize(n*2, unused);
    }
    void propagate(int x, int nl, int nr){
        if(lazy[x] == unused) return;
        if(x < n){
            lazy[x*2] = combineL(lazy[x*2], lazy[x]);
            lazy[x*2+1] = combineL(lazy[x*2+1], lazy[x]);
        }
        unlazy(x, nl, nr);
        lazy[x] = unused;
    }
    void update(int l, int r, T2 val){update(l, r, val, 1, 0, n-1);}
    void update(int l, int r, T2 val, int x, int nl, int nr){
        propagate(x, nl, nr);
        if(r < nl || nr < l) return;
        if(l <= nl && nr <= r){
            lazy[x] = combineL(lazy[x], val);
            propagate(x, nl, nr);
            return;
        }
        int mid = (nl + nr) / 2;
        update(l, r, val, x*2, nl, mid); update(l, r, val, x*2+1, mid+1, nr);
        arr[x] = combine(arr[x*2], arr[x*2+1]);
    }
    T1 query(int l, int r){return query(l, r, 1, 0, n-1);}
    T1 query(int l, int r, int x, int nl, int nr){
        propagate(x, nl, nr);
        if(r < nl || nr < l) return id;
        if(l <= nl && nr <= r) return arr[x];
        int mid = (nl + nr) / 2;
        return combine(query(l, r, x*2, nl, mid), query(l, r, x*2+1, mid+1, nr));
    }
};