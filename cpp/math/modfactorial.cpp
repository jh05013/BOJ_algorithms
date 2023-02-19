struct Modfact{
	vector<modint> fact, ifact;
	Modfact(int n): fact(n+1), ifact(n+1){
		fact[0] = 1;
		for(int i=1; i<=n; i++) fact[i] = fact[i-1] * (modint)i;
		ifact[n] = inv(fact[n]);
		for(int i=n-1; i>=0; i--) ifact[i] = ifact[i+1] * (modint)(i+1);
	}

	modint operator[](int i){return fact[i];}
	modint binom(int n, int k){
		if(k > n) return 0;
		return fact[n] * ifact[k] * ifact[n-k];
	}
};
