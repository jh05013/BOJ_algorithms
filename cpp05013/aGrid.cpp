template <typename T>
struct Grid{
    int n, m; vector<vector<T>> arr;
    int di[4] = {-1,0,1,0};
    int dj[4] = {0,-1,0,1};
    Grid(int n, int m): n{n}, m{m}, arr(n, vector<T>(m)) {}
    bool ingrid(int i, int j){return 0<=i && i<n && 0<=j && j<m;}
    void input(){for(int i=0; i<n; i++)for(int j=0; j<m; j++) cin>>arr[i][j];}
};