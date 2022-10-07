template <typename T>
T euler_phi(T n){
	if(n <= 1) return 0;
	ll ans = n;
	for(int d=2; d*d<=n; d++) if(n%d == 0){
		ans = ans*(d-1)/d;
		while(n%d == 0) n/= d;
	}
	if(n > 1) ans = ans*(n-1)/n;
	return (T)ans;
}
