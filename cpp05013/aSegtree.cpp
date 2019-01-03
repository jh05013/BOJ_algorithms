// 0-indexed
template <typename T>
struct Segtree{
    T id = 2147483647;
    T combine(T a, T b){
        return min(a, b);
    }
    
    int n; vector<T> arr;
    Segtree(int sz): n{1} {
        while(n < sz) n<<=1;
        arr.resize(n*2);
    }
    void construct(vector<T>& A){
        for(size_t i=0; i<A.size(); i++) arr[n+i]= A[i];
        for(int i=n-1; i>=0; i--) arr[i] = combine(arr[2*i], arr[2*i+1]);
    }
    void update(int i, T val){
        for(arr[i+=n] = val; i > 1; i/= 2) arr[i/2] = combine(arr[i], arr[i^1]);
    }
    T query(int l, int r){
        T resl = id, resr = id;
        for(l+= n, r+= n+1; l < r; l/= 2, r/= 2){
            if(l&1) resl = combine(resl, arr[l++]);
            if(r&1) resr = combine(resr, arr[--r]);
        }
        return combine(resl, resr);
    }
};