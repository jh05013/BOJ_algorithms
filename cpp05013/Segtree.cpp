// 0-indexed
struct Segtree{
    typedef ll T; // Change this to what you need
    T id = 0;
    T combine(T a, T b){
        // The value when a <-- b
    }

    int n; vector<T> arr;
    Segtree(int sz): n{1} {while(n < sz) n<<=1; arr.resize(n*2, id);}

    void update(int i, T v){
        for(arr[i+=n]=v; i>>=1;) arr[i] = combine(arr[i<<1], arr[i<<1|1]);
    }
    T query(int l, int r){
        T resl=id, resr=id;
        for(l+= n, r+= n+1; l < r; l/= 2, r/= 2){
            if(l&1) resl = combine(resl, arr[l++]);
            if(r&1) resr = combine(arr[--r], resr);
        }
        return combine(resl, resr);
    }
};