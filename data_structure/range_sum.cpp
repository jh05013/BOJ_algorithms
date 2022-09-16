template<typename T>
struct RangeSum{
	int n;
	vector<T> arr;

	RangeSum(vector<T> A): n(sz(A)), arr(A) {
		for(int i=1; i<n; i++) arr[i]+= arr[i-1];
	}

	T sum(int l, int r){
		assert(0 <= l && l <= r && r < n);
		return arr[r] - (l? arr[l-1] : 0);
	}
	T sum_generous(int l, int r){
		if(l > r) return 0;
		return sum(max(0, l), min(n-1, r));
	}
};
