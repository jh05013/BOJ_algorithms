/* SZ N
 * 15 32768
 * 16 65536
 * 17 131072
 * 18 262144
 * 19 524288
 * 20 1048576
 */

const int SZ = 20, N = 1 << SZ;
 
int Rev(int x){
    int r = 0;
    for(int i=0; i<SZ; i++) r = r<<1 | (x&1), x>>= 1;
    return r;
}
void FFT(vector<ll> &A, bool f){
    for(int i=0; i<N; i++){
        int j = Rev(i);
        if (i < j) swap(A[i], A[j]);
    }
    for(int i=1; i<N; i<<=1) for(int j=0; j<N; j+=i<<1)
    for(int k=0; k<i; k++){
        ll u = A[j+k], v = A[i+j+k];
        if(f) A[j+k] = v-u, A[i+j+k] = u;
        else A[j+k] = v, A[i+j+k] = u+v;
    }
}

vector<ll> multiply(vector<ll> X, vector<ll> Y){
    FFT(X, 0), FFT(Y, 0);
    for(int i=0; i<N; i++) X[i]*= Y[i];
    FFT(X, 1);
    return X;
}