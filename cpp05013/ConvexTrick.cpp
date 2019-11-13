// dp[i] = min_j(a[j]*x[i] + b[j]) + const[i] where the slopes are monotonic

// Assumption x[i] <= x[i+1], decreasing slopes
template <typename T>
struct CHT{
    vector<pair<T,T>> hull; int p=0;
    long double cr(int x){
        auto [ax,bx] = hull[x]; auto [ay,by] = hull[x+1];
        return (long double)(by-bx) / (ax-ay);
    }

    void insert(T a, T b){
        hull.push_back({a,b});
        while(hull.size() > 2 && cr(hull.size()-3) >
            cr(hull.size()-2)) hull.erase(hull.end()-2);
    }

    T get(T x){
        while(p+1 < hull.size() && cr(p) <= x) p++;
        auto [a,b] = hull[p];
        return a*x + b;
    }
};