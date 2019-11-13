struct PST{
    typedef ll T; // Change this to what you need
    T id = 0;
    T combine(T a, T b){
        // The value when a <-- b
        return a + b;
    }

    vector<T> arr;
    vector<int> L, R, root;
    int N = 1;

    // Initialize with 0..N-1, root = 0
    PST(int n){
        while(N < n) N<<= 1;
        root.push_back(create(0, N-1));
    }
    int create(int l, int r){
        int k = arr.size();
        arr.push_back(id), L.push_back(-1), R.push_back(-1);
        if(l < r){
            int m = (l+r)/2;
            L[k] = create(l, m);
            R[k] = create(m+1, r);
        }
        return k;
    }

    // Add v to [p] at time t, returns root
    int add(int t, int p, int v){
        if(t == -1) t = root.back();
        root.push_back(add(0, N-1, t, p, v));
        return root.back();
    }
    int add(int l, int r, int t, int p, int v){
        if(!(l<=p && p<=r)) return t;
        int k = arr.size();
        arr.push_back(id), L.push_back(-1), R.push_back(-1);
        if(l == r) arr[k] = combine(arr[t], v);
        else{
            int m = (l+r)/2;
            L[k] = add(l, m, L[t], p, v);
            R[k] = add(m+1, r, R[t], p, v);
            arr[k] = combine(arr[L[k]], arr[R[k]]);
        }
        return k;
    }

    // Query [l, r] at time t
    T query(int t, int l, int r){return query(0, N-1, t, l, r);}
    T query(int l, int r, int t, int ql, int qr){
        if(ql<=l && r<=qr) return arr[t];
        if(ql>r || l>qr) return id;
        int m = (l+r)/2;
        return combine(query(l,m,L[t],ql,qr), query(m+1,r,R[t],ql,qr));
    }
};