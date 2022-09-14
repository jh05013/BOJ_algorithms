const int CDSZ = 400;
const int CDCNT = 2500;
TTT struct CountDistinct{
	int n;
	vector<int> prv, nxt;
	int bsum[CDCNT][CDCNT];

	CountDistinct(vector<T> V): n{sz(V)}, prv(n,-1), nxt(n,n) {
		assert(n <= CDSZ * CDCNT);
		memset(bsum, 0, sizeof bsum);
		map<T, int> prvlast, nxtlast;
		for(int i=0; i<n; i++){
			if(prvlast.find(V[i]) != prvlast.end()) prv[i] = prvlast[V[i]];
			if(prv[i] != -1) bsum[i/CDSZ][prv[i]/CDSZ]++;
			prvlast[V[i]] = i;
		}
		for(int i=n-1; i>=0; i--){
			if(nxtlast.find(V[i]) != nxtlast.end()) nxt[i] = nxtlast[V[i]];
			nxtlast[V[i]] = i;
		}
		for(int i=0; i<CDCNT; i++) for(int j=0; j<CDCNT; j++){
			if(i) bsum[i][j]+= bsum[i-1][j];
			if(j) bsum[i][j]+= bsum[i][j-1];
			if(i && j) bsum[i][j]-= bsum[i-1][j-1];
		}
	}

	int query(int l, int r){
		assert(0 <= l && l <= r && r < n);
		int bl = l? (l-1)/CDSZ+1 : 0, br = (r+1)/CDSZ-1, ans = 0;
		if(bl > br){
			for(int i=l; i<=r; i++) ans+= (prv[i] >= l);
			return r-l+1 - ans;
		}
		ans = bsum[br][br];
		if(bl) ans-= bsum[bl-1][br] + bsum[br][bl-1] - bsum[bl-1][bl-1];
		bl*= CDSZ, br = (br+1)*CDSZ-1;
		for(; bl>l; bl--) ans+= (nxt[bl-1] <= br);
		for(; br<r; br++) ans+= (prv[br+1] >= l);
		return r-l+1 - ans;
	}
};
