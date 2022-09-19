template<typename T>
struct CartesianTree{
	int n, root = -1;
	vector<int> P, L, R;
	CartesianTree(vector<T> arr): n{sz(arr)},
		P(sz(arr), -1), L(sz(arr), -1), R(sz(arr), -1) {
		vector<int> ls(n, -1), rs(n, -1);
		stack<pair<T, int>> S;
		for(int i=0; i<n; i++){
			T x = arr[i];
			while(!S.empty() && S.top().first > x) S.pop();
			if(!S.empty()) ls[i] = S.top().second;
			S.push({x, i});
		}
		while(!S.empty()) S.pop();
		for(int i=n-1; i>=0; i--){
			T x = arr[i];
			while(!S.empty() && S.top().first >= x) S.pop();
			if(!S.empty()) rs[i] = S.top().second;
			S.push({x, i});
		}
		for(int i=0; i<n; i++){
			if(ls[i] == -1 && rs[i] == -1){root = P[i] = i; continue;}
			int xl = (ls[i] != -1)? arr[ls[i]] : -1;
			int xr = (rs[i] != -1)? arr[rs[i]] : -1;
			if(xl > xr) P[i] = ls[i], R[ls[i]] = i;
			else P[i] = rs[i], L[rs[i]] = i;
		}
	}
};
