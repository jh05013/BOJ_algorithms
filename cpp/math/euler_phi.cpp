template<typename T>
T phi(T n){
	if(n <= 1) return 0;
	T phi = n;
	for(T p=2; p*p<=n; p++) if(n%p == 0){
		phi = phi/p*(p-1);
		while(n%p == 0) n/= p;
	}
	if(n > 1) phi = phi/n*(n-1);
	return phi;
}
