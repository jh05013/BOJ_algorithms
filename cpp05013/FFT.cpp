/* SZ N
 * 15 32768
 * 16 65536
 * 17 131072
 * 18 262144
 * 19 524288
 * 20 1048576
 */

int SZ = 19, N = 1<<SZ;

int Rev(int x){
    int r = 0;
    for(int i=0; i<SZ; i++) r = r<<1 | (x&1), x>>= 1;
    return r;
}
const double PI = acos(-1);
typedef complex<double> CD;
typedef vector<CD> VCD;
void FFT(VCD& A, int f){
    CD x, y, z;
    for(int i=0; i<N; i++){
        int j = Rev(i);
        if(i < j) swap(A[i], A[j]);
    }
    for(int i=1; i<N; i<<= 1){
        double w = PI / i;
        if(f) w = -w;
        CD x(cos(w), sin(w));
        for(int j=0; j<N; j+= i<<1){
            CD y(1);
            for(int k=0; k<i; k++){
                CD z = A[i+j+k] * y;
                A[i+j+k] = A[j+k] - z, A[j+k]+= z;
                y*= x;
            }
        }
    }
    if(f) for(int i=0; i<N; i++) A[i]/= N;
}

vector<int> square(VCD X){
    FFT(X, 0);
    for(int i=0; i<N; i++) X[i]*= X[i];
    FFT(X, 1);
    vector<int> res(N);
    for(int i=0; i<N; i++) res[i] = round(X[i].real());
    return res;
}

vector<int> multiply(VCD X, VCD Y){
    FFT(X, 0), FFT(Y, 0);
    for(int i=0; i<N; i++) X[i]*= Y[i];
    FFT(X, 1);
    vector<int> res(N);
    for(int i=0; i<N; i++) res[i] = round(X[i].real());
    return res;
}

void thinksmall(){
    int n, m, x; cin>>n>>m;
    while(n+m+2 > N) SZ++, N<<=1;
    VCD A(N), B(N), AR(N), BR(N);
    
    for(int i=0; i<n+1; i++) cin>>x, A[i] = CD(x>>10, x&1023);
    for(int i=0; i<m+1; i++) cin>>x, B[i] = CD(x>>10, x&1023);
    FFT(A, 0); FFT(B, 0);
    for(int i=0; i<N; i++){
        int j = i? N-i : i;
        CD f1 = (A[i] + conj(A[j])) / CD(2, 0), f2 = (A[i] - conj(A[j])) / CD(0, 2),
           f3 = (B[i] + conj(B[j])) / CD(2, 0), f4 = (B[i] - conj(B[j])) / CD(0, 2);
        AR[i] = f1 * (f3 + f4 * CD(0, 1)), BR[i] = f2 * (f3 + f4 * CD(0, 1));
    }
    FFT(AR, 1); FFT(BR, 1);
    ll ans = 0;
    for(int i=0; i<n+m+2; i++){
        ll ar = roundl(real(AR[i])) + 0.01, ai = roundl(imag(AR[i])) + 0.01,
           br = roundl(real(BR[i])) + 0.01, bi = roundl(imag(BR[i])) + 0.01;
        ll res = bi + ((ai + br) << 10) + (ar << 20);
        ans^= res;
    }
    cout << ans;
}