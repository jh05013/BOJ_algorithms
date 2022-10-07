template <typename T>
T linear_modmin_rec(T a, T b, T N, T e){
	if(e <= 10){
		ll ans = b;
		for(ll x=1; x<=e; x++) ans = min(ans, (a*x+b)%N);
		return ans;
	}
	if(2*a > N) return linear_modmin_rec(N-a, (a*e+b)%N, N, e);
	if(a*e+b < N) return b;
	ll s = b + a*((N-b+a-1)/a) - N;
	return min(b, linear_modmin_rec(((-N)%a+a)%a, s, a, (a*e+b)/N - 1));
}

// minimum (ax+b)%N for x = 0, ..., e
template <typename T>
T linear_modmin(T a, T b, T N, T e){
	assert(a >= 0 && b >= 0 && N > 0 && e >= 0);
	a%= N, b%= N;
	T g = __gcd(a, N);
	if(g != 1) return g * linear_modmin_rec(a/g, b/g, N/g, e) + b%g;
	return linear_modmin_rec(a, b, N, e);
}
