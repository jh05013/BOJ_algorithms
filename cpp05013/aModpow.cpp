// int/ll modpow
template <class T>
T pow(T a, ll x, T mod){
    a%= mod; T r;
    for(r=1; x; x/=2){if(x%2) r = r*a%mod; a = a*a%mod;}
    return r;
}

template <class T>
T ncr(int n, int r, T p){
    T r = 1;
    for(int i=0; i<r; i++){
        r = (r*(n-i)) % p;
        r = (r*pow(i+1, p-2, p)) % p;
    }
    return r;
}

// Rectangular matrix
template <typename T>
struct Matrix{
    int n, m; vector<vector<T>> mat;
    Matrix(int n, int m) :n{n}, m{m}, mat{vector<vector<T>>(n, vector<T>(m))} {}
    Matrix operator*(Matrix& B){
        if(m != B.n) throw exception();
        Matrix ans = Matrix(n, B.m);
        for(int i=0; i<n; i++) for(int j=0; j<B.m; j++) for(int b=0; b<m; b++)
            ans.mat[i][j]+= mat[i][b]*B.mat[b][j];
        return ans;
    }
    void input(){for(int i=0; i<n; i++) for(int j=0; j<m; j++) cin>>mat[i][j];}
};

// Square matrix modpow
template <typename T>
struct Matrix{
    int n; T mod; vector<vector<T>> mat;
    Matrix(int n) :n{n}, mat(n, vector<T>(n)) {}
    Matrix operator*(Matrix& B){
        Matrix ans = Matrix(n);
        for(int i=0; i<n; i++) for(int j=0; j<n; j++) for(int b=0; b<n; b++)
            ans.mat[i][j]+= mat[i][b]*B.mat[b][j];
        return ans;
    }
    Matrix operator%(T mod){
        Matrix ans = Matrix(n);
        for(int i=0; i<n; i++) for(int j=0; j<n; j++) ans.mat[i][j] = mat[i][j]%mod;
        return ans;
    }
    void input(){for(int i=0; i<n; i++) for(int j=0; j<n; j++) cin>>mat[i][j];}
};

template <class T>
Matrix<T> matpow(Matrix<T> A, ll x, T mod){
    A = A%mod; Matrix<T> r(A.n);
    for(int i=0; i<A.n; i++) r.mat[i][i] = 1;
    for(; x; x/=2){if(x%2) r = r*A%mod; A = A*A%mod;}
    return r;
}