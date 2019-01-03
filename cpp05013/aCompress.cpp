template <typename T>
struct Compress{
    int n; vector<T> arr;
    void add(T x){arr.push_back(x); n++;}
    void init(){sort(entire(arr));}
    int lb(T x){return lower_bound(entire(arr), x) - arr.begin();}
    int ub(T x){return upper_bound(entire(arr), x) - arr.begin();}
};

// you may add unique(entire(arr)) in the init function