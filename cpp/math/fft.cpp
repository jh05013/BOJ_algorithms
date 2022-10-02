const long double PI = acos(-1);
template <typename DT>
void FFT(vector<complex<DT>> &A, bool inv){
	int n = A.size();
	for(int i=1, j=0; i<n; i++){
		for(int k=n>>1; (j^=k)<k; k>>= 1);
		if(i < j) swap(A[i], A[j]);
	}
	for(int i=1; i<n; i<<= 1){
		DT w = (DT)PI / i;
		if(inv) w = -w;
		complex<DT> x(cos(w), sin(w));
		for(int j=0; j<n; j+= i<<1){
			complex<DT> y(1);
			for(int k=0; k<i; k++){
				complex<DT> z = A[i+j+k]*y;
				A[i+j+k] = A[j+k]-z, A[j+k]+= z;
				y*= x;
			}
		}
	}
	if(inv) for(int i=0; i<n; i++) A[i]/= n;
}

template <typename T, typename DT>
vector<T> polymul(vector<T> X, vector<T> Y){
	int n, xy = sz(X)+sz(Y);
	for(n=1; n<xy; n<<= 1);
	vector<complex<DT>> A(n), B(n);
	for(int i=0; i<sz(X); i++) A[i] = X[i];
	for(int i=0; i<sz(Y); i++) B[i] = Y[i];
	FFT(A, 0), FFT(B, 0);
	for(int i=0; i<n; i++) A[i]*= B[i];
	FFT(A, 1);
	vector<T> res(xy);
	for(int i=0; i<xy; i++){
		DT x = A[i].real();
		res[i] = (T)(x + 0.5 - (x<0));
		assert(abs(A[i].real() - res[i]) < 0.2);
	}
	return res;
}
