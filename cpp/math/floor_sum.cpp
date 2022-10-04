template <typename T>
T floor_sum(T n, T m, T a, T b){
	assert(0 <= n && 1 <= m);
	T ans = 0;
	if(a >= m || a < 0) ans+= (n-1)*n/2 * (a/m), a%= m;
	if(b >= m || b < 0) ans+= n * (b/m), b%= m;
	if(a == 0) return ans;
	ll y = (a*n+b)/m, z = (a*n+b)%m;
	return ans + floor_sum(y, a, m, z);
}
