// minimalistic, 0-indexed
template <typename T>
struct Fenwick{
    int n; vector<T> arr;
    Fenwick(int n): n{n}, arr(n) {}
    void add(int i, T val){
        while(i < n) arr[i]+= val, i |= i+1;
    }
    T getsum(int i){
        T res = 0;
        while(i >= 0) res+= arr[i], i = (i&(i+1))-1;
        return res;
    }
};



// 0-indexed
template <typename T>
struct Fenwick{
    int n; vector<T> arr;
    Fenwick(int n): n{n}, arr(n) {}
    void construct(vector<T>& A){
        for(int i=0; i<n; i++) arr[i] = A[i];
        for(int i=0; i<n; i++) if((i|(i+1)) < n) arr[i|(i+1)]+= arr[i];
    }
    void add(int i, T val){
        while(i < n) arr[i]+= val, i |= i+1;
    }
    T getsum(int i){
        T res = 0;
        while(i >= 0) res+= arr[i], i = (i&(i+1))-1;
        return res;
    }
    T intersum(int i, int j){
        return i? (getsum(j) - getsum(i-1)) : getsum(j);
    }
};



template <typename T>
struct FenwickRUPQ{
    int n; vector<T> arr;
    Fenwick(int n): n{n}, arr(n) {}
    void add(int i, int j, T val){
        while(i < n) arr[i]+= val, i |= i+1;
        j++;
        while(j < n) arr[j]-= val, j |= j+1;
    }
    T get(int i){
        T res = 0;
        while(i >= 0) res+= arr[i], i = (i&(i+1))-1;
        return res;
    }
};



struct RangeFenwick{
    vector<ll> arrmul, arradd;
    RangeFenwick(int n): arrmul(n), arradd(n){}
    void update(int l, int r, ll val){
        zeroupdate(l, val, -val*(l-1));
        zeroupdate(r, -val, val*r);
    }
    ll intersum(int i, int j){
        return getsum(j) - getsum(i-1);
    }

    void zeroupdate(int i, ll mul, ll add){
        for(; i<arrmul.size(); i|=i+1) arrmul[i]+= mul, arradd[i]+= add;
    }
    ll getsum(int i){
        ll mul = 0, add = 0, start = i;
        for(; i>=0; i=(i&(i+1))-1) mul+= arrmul[i], add+= arradd[i];
        return mul*start + add;
    }
};