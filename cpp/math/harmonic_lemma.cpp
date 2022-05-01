// vector of {x, l, r} s.t n/i == x for i in [l, r]
TTT vector<tuple<T,T,T>> harmonic_floor(T n){
	assert(n > 0);
	vector<tuple<T,T,T>> ans;
	T i = 1;
	for(; n/i != n/(i+1); i++) ans.push_back({n/i, i, i});
	for(T v = n/i; v >= 1; v--) ans.push_back({v, n/(v+1)+1, n/v});
	return ans;
}

// vector of {x, l, r} s.t ceil(n/i) == x for i in [l, r]
TTT T cdiv(T a, T b){return (a-1)/b+(T)1;}
TTT vector<tuple<T,T,T>> harmonic_ceil(T n){
	assert(n > 0);
	vector<tuple<T,T,T>> ans;
	T i = 1;
	for(; cdiv(n,i) != cdiv(n,i+1); i++) ans.push_back({cdiv(n,i), i, i});
	for(T v = cdiv(n,i); v >= 2; v--) ans.push_back({v, cdiv(n,v), cdiv(n,v-1)-1});
	return ans;
}

// {x, y, l, r} s.t n/i == x and m/i == y for i in [l, r]
TTT vector<tuple<T,T,T,T>> harmonic2_floor(T n, T m){
	assert(n > 0 && m > 0);
	vector<tuple<T,T,T>> ah = harmonic_floor(n), bh = harmonic_floor(m);
	vector<tuple<T,T,T,T>> ans;
	int ai = 0, bi = 0;
	while(ai < sz(ah) && bi < sz(bh)){
		auto [av, al, ar] = ah[ai];
		auto [bv, bl, br] = bh[bi];
		if(ar < br) ans.push_back({av,bv,al,ar}), ai++, bh[bi] = {bv,ar+1,br};
		else if(ar == br) ans.push_back({av,bv,al,ar}), ai++, bi++;
		else ans.push_back({av,bv,bl,br}), bi++, ah[ai] = {av,br+1,ar};
	}
	return ans;
}
