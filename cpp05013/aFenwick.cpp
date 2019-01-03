// 0-indexed
template <typename T>
struct Fenwick{
    int n; vector<T> arr;
    Fenwick(int n): n{n}, arr(n) {}
    void construct(vector<T>& A){
        for(int i=0; i<n; i++) arr[i] = A[i];
        for(int i=0; i<n; i++) if((i|(i+1)) < n) arr[i|(i+1)]+= arr[i];
    }
    void update(int i, T val){
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
    void update(int i, int j, T val){
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