// Fenwick tree that supports k-th element in O(logn)
// k is 1-indexed

struct Fenwick{
    int lsz = 0;
    vector<ll> arr;
    Fenwick(int n){
        int sz = 1;
        while(sz < n) lsz++, sz<<= 1;
        arr.resize(sz);
    }

    void add(int i, ll val){
        while(i < arr.size()) arr[i]+= val, i|= i+1;
    }
    ll getsum(int i){
        ll res = 0;
        while(i >= 0) res+= arr[i], i = (i&(i+1))-1;
        return res;
    }
    int kth(int k){
        int l = 0, r = arr.size();
        for(int i=0; i<=lsz; i++){
            int mid = (l+r)>>1;
            ll val = arr[mid-1];
            if(val >= k) r = mid;
            else l = mid, k-= val;
        }
        return l;
    }
};