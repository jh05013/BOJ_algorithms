// 0-indexed
// the T conversion is not verified, CHECK IT YOURSELF
const int INF = 2147483647;
template <typename T>
T hungarian(vector<vector<T>>& mat){
    int n = mat.size(), m = mat[0].size();
    vector<T> u(n+1), v(m+1), p(m+1), way(m+1), minv(m+1);
    vector<char> used(m+1);
    for(int i=1; i<=n; ++i) {
        int j0 = 0; p[0] = i;
        fill(entire(minv), INF);
        fill(entire(used), false);
        while(1){
            used[j0] = true;
            int i0 = p[j0], j1; T delta = INF;
            for (int j=1; j<=m; ++j) if(!used[j]) {
                T cur = mat[i0-1][j-1] - u[i0] - v[j];
                if (cur < minv[j]) minv[j] = cur, way[j] = j0;
                if (minv[j] < delta) delta = minv[j], j1 = j;
            }
            for (int j=0; j<=m; ++j) {
                if (used[j]) u[p[j]] += delta, v[j] -= delta;
                else minv[j] -= delta;
            }
            j0 = j1;
            if(p[j0] == 0) break;
        }
        while(1){
            T j1 = way[j0];
            p[j0] = p[j1]; j0 = j1;
            if(!j0) break;
        }
    }
    //for (int j = 1; j <= m; ++j) matched[p[j]] = j;
    return -v[0];
}