template <typename T>
T max_sumarray(vector<T> arr){
	assert(!arr.empty());
	T best = arr[0], cur = 0;
	for(T &x: arr){
		cur+= x;
		best = max(best, cur);
		if(cur < 0) cur = 0;
	}
	return best;
}
