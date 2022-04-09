vector<int> z_algo(string& s){
	int n = s.size(), L=0, R=0;
	vector<int> z(n); z[0] = n;
	for(int i=1; i<n; i++){
		if(i > R){
			L = R = i;
			while(R < n && s[R-L] == s[R]) R++;
			z[i] = R-L; R--;
			continue;
		}
		int k = i - L;
		if(z[k] < R-i+1) z[i] = z[k];
		else{
			L = i;
			while(R < n && s[R-L] == s[R]) R++;
			z[i] = R-L; R--;
		}
	}
	return z;
}

template <typename T>
vector<int> z_algo(vector<T>& s){
	int n = s.size(), L=0, R=0;
	vector<int> z(n); z[0] = n;
	for(int i=1; i<n; i++){
		if(i > R){
			L = R = i;
			while(R < n && s[R-L] == s[R]) R++;
			z[i] = R-L; R--;
			continue;
		}
		int k = i - L;
		if(z[k] < R-i+1) z[i] = z[k];
		else{
			L = i;
			while(R < n && s[R-L] == s[R]) R++;
			z[i] = R-L; R--;
		}
	}
	return z;
}