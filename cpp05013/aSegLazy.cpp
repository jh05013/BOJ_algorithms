// 0-indexed
template <typename T>
struct Segtree{
    T id = 0;
    T unused = 0;
    T combine(T a, T b){
        // What is the combined value of a and b?
        return a+b;
    }
    T combineL(T a, T b){
        // What is the new lazy value when a is updated with b?
        return a+b;
    }
    void unlazy(int x, int nl, int nr){
        // What is the value if the lazy value is applied?
        arr[x]+= lazy[x] * (nr-nl+1);
    }
    
    int n; vector<T> arr, lazy;
    Segtree(int sz): n{1} {
        while(n < sz) n<<=1;
        arr.resize(n*2); lazy.resize(n*2);
    }
    void construct(vector<T>& A){
        for(size_t i=0; i<A.size(); i++) arr[n+i]= A[i];
        for(int i=n-1; i>=0; i--) arr[i] = combine(arr[2*i], arr[2*i+1]);
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
    void update(int l, int r, T val){update(l, r, val, 1, 0, n-1);}
    void update(int l, int r, T val, int x, int nl, int nr){
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
    T query(int l, int r){return query(l, r, 1, 0, n-1);}
    T query(int l, int r, int x, int nl, int nr){
        propagate(x, nl, nr);
        if(r < nl || nr < l) return id;
        if(l <= nl && nr <= r) return arr[x];
        int mid = (nl + nr) / 2;
        return combine(query(l, r, x*2, nl, mid), query(l, r, x*2+1, mid+1, nr));
    }
};