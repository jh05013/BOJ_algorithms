template <typename T>
struct Fenwick2D{
	int n = 1, m = 1, real_n, real_m;
	vector<vector<T>> arr, content;
	Fenwick2D(int N, int M): real_n(N), real_m(M){
		while(n < N) n<<= 1;
		while(m < M) m<<= 1;
		arr.resize(n, vector<T>(m));
		content.resize(real_n, vector<T>(real_m));
	}

	void add(int i, int j, T val){
		assert(0 <= i && i < real_n && 0 <= j && j < real_m);
		content[i][j]+= val;
		for(int x=i; x<n; x|= x+1)
		for(int y=j; y<m; y|= y+1) arr[x][y]+= val;
	}
	void change(int i, int j, T val){
		assert(0 <= i && i < real_n && 0 <= j && j < real_m);
		add(i, j, val-content[i][j]);
	}
	T sum(int i, int j){
		assert(0 <= i && i < real_n && 0 <= j && j < real_m);
		T res = 0;
		for(int x=i; x>=0; x = (x&(x+1))-1)
		for(int y=j; y>=0; y = (y&(y+1))-1) res+= arr[x][y];
		return res;
	}
	T sum(int i1, int j1, int i2, int j2){
		assert(0 <= i1 && i1 <= i2 && i2 < real_n);
		assert(0 <= j1 && j1 <= j2 && j2 < real_m);
		T ans = sum(i2, j2);
		if(i1) ans-= sum(i1-1, j2);
		if(j1) ans-= sum(i2, j1-1);
		if(i1 && j1) ans+= sum(i1-1, j1-1);
		return ans;
	}
};
