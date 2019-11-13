template <typename T>
struct Sum2d{
    int n, m; vector<vector<T>> arr;
    Sum2d(int n, int m): n{n}, m{m}, arr(n, vector<T>(m)) {}
    T get(int i, int j){
        i = min(i,n-1); j = min(j,m-1);
        return (0<=i && 0<=j)? arr[i][j] : 0;
    }
    void init(){
        for(int i=0; i<n; i++) for(int j=0; j<m; j++)
            arr[i][j]+= get(i-1,j) + get(i,j-1) - get(i-1,j-1);
    }

    T getsum(int i1, int j1, int i2, int j2){
        return get(i2,j2) - get(i1-1,j2) - get(i2,j1-1) + get(i1-1,j1-1);
    }
};