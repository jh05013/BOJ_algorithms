TTT struct Fenwick{
	int lsz = 0;
	vector<T> arr, content;
	Fenwick(int n){
		int sz = 1;
		while(sz < n) lsz++, sz<<= 1;
		arr.resize(sz), content.resize(sz);
	}

	void add(int i, T val){
		content[i]+= val;
		while(i < sz(arr)) arr[i]+= val, i|= i+1;
	}
	void change(int i, T val){add(i, val-content[i]);}
	T sum(int i){
		T res = 0;
		while(i >= 0) res+= arr[i], i = (i&(i+1))-1;
		return res;
	}
	T sum(int i, int j){return sum(j)-(i? sum(i-1):0);}
	// kth is 1-indexed
	int kth(T k){
		assert(arr.back() >= k);
		int l = 0, r = sz(arr);
		for(int i=0; i<=lsz; i++){
			int mid = (l+r)>>1;
			ll val = mid? arr[mid-1]:arr.back();
			if(val >= k) r = mid;
			else l = mid, k-= val;
		}
		return l;
	}
};
