const int MOD = 998244353;
const int PRIMITIVE_ROOT = 3;

struct modint{
	int val;
	modint(): val{0} {}
	modint(const ll &v){
		val = (-MOD <= v && v < MOD)? (int)v:(int)(v%MOD);
		if(val < 0) val+= MOD;
	}
	friend istream& operator>>(istream& is, modint& a){
		ll v; is>>v;
		a.val = (-MOD <= v && v < MOD)? (int)v:(int)(v%MOD);
		if(a.val < 0) a.val+= MOD;
		return is;
	}
	friend ostream& operator<<(ostream& os, const modint& a){return os<<a.val;}
	friend bool operator==(const modint& a, const modint& b){return a.val==b.val;}
	friend bool operator!=(const modint& a, const modint& b){return a.val!=b.val;}
	friend bool operator<(const modint& a, const modint& b){return a.val<b.val;}

	modint operator-() const {return modint(-val);}
	modint& operator+=(const modint& m){if((val+=m.val)>=MOD) val-= MOD; return *this;}
	modint& operator-=(const modint& m){if((val-=m.val)<0) val+= MOD; return *this;}
	modint& operator*=(const modint& m){val = (int)((ll)val*m.val%MOD); return *this;}

	friend modint ipow(modint a, ll p){
		assert(p >= 0);
		modint ans = 1;
		for(; p; p/=2, a*=a) if(p&1) ans*= a;
		return ans;
	}
	friend modint inv(const modint& a){
		assert(a.val);
		return ipow(a, MOD-2);
	}
	modint& operator/=(const modint& m){return (*this)*= inv(m);}

	friend modint operator+(modint a, const modint& b){return a+= b;}
	friend modint operator-(modint a, const modint& b){return a-= b;}
	friend modint operator*(modint a, const modint& b){return a*= b;}
	friend modint operator/(modint a, const modint& b){return a/= b;}
	operator int64_t() const {return val;}
};

struct modpoly{
	vector<modint> P;

	//// INIT & BASIC
	modpoly(int n): P(n) {}
	modpoly(vector<modint> A): P(A) {}
	modint& operator[](int i){return P[i];}
	int size(){return sz(P);}
	bool empty(){return P.empty();}
	void normalize(){while(!empty() && P.back() == (modint)0) P.pop_back();}
	
	//// TRIVIAL OPS
	void resize(int n){P.resize(n);}
	modpoly resized(int n){
		modpoly Q(n);
		for(int i=0; i<min(n, size()); i++) Q[i] = P[i];
		return Q;
	}
	void push_back(modint x){P.push_back(x);}
	void reverse(){std::reverse(P.begin(), P.end());}

	//// IO
	friend istream& operator>>(istream &is, modpoly &p){
		for(int i=0; i<p.size(); i++) is>>p[i];
		return is;
	}
	friend ostream& operator<<(ostream &os, const modpoly &p){
		for(modint x:p.P) os<<x<<' ';
		return os;
	}

	//// PLUS, MINUS
	modpoly operator-() const {
		modpoly M(P); for(int i=0; i<M.size(); i++) M[i] = -M[i];
		return M;
	}
	modpoly& operator+=(modpoly q){
		if(size() < q.size()) resize(q.size());
		for(int i=0; i<q.size(); i++) P[i]+= q[i];
		return *this;
	}
	friend modpoly operator+(modpoly p, modpoly q){return p+= q;}
	modpoly& operator-=(modpoly q){
		if(size() < q.size()) resize(q.size());
		for(int i=0; i<q.size(); i++) P[i]-= q[i];
		return *this;
	}
	friend modpoly operator-(modpoly p, modpoly q){return p-= q;}

	//// CALCULUS
	modpoly derivative(){
		modpoly q(max(0, size()-1));
		for(int i=1; i<size(); i++) q[i-1] = (modint)i * P[i];
		return q;
	}
	modpoly integral(){
		modpoly q(size()+1);
		for(int i=0; i<size(); i++) q[i+1] = P[i] / (modint)(i+1);
		return q;
	}

	//// FFT
	void fft(bool inv){
		int n = size();
		for(int i=1, j=0; i<n; i++){
			for(int k=n>>1; (j^=k)<k; k>>= 1);
			if(i < j) swap(P[i], P[j]);
		}
		modint RINV = ipow((modint)PRIMITIVE_ROOT, MOD-2);
		for(int i=1; i<n; i<<= 1){
			modint x = inv? RINV : (modint)PRIMITIVE_ROOT;
			x = ipow(x, MOD/i>>1);
			for(int j=0; j<n; j+= i<<1){
				modint y = 1;
				for(int k=0; k<i; k++){
					modint z = P[i+j+k]*y;
					P[i+j+k] = P[j+k]-z, P[j+k]+= z;
					y*= x;
				}
			}
		}
		modint NINV = ipow((modint)n, MOD-2);
		if(inv) for(int i=0; i<n; i++) P[i]*= NINV;
	}
	modpoly& operator*=(modpoly q){
		int n, xy = size()+q.size();
		for(n=1; n<xy; n<<= 1);
		resize(n), q.resize(n);
		fft(0), q.fft(0);
		for(int i=0; i<n; i++) P[i]*= q[i];
		fft(1); resize(xy-1);
		return *this;
	}
	friend modpoly operator*(modpoly p, modpoly q){return p*= q;}

	//// DIVISION
	modpoly inv(int d){
		assert(P[0] != (modint)0);
		modpoly I(1); I[0] = modint(1) / P[0];
		for(int n=1; n<d; n*= 2){
			modpoly f = resized(2*n), g = I.resized(2*n);
			f.fft(0), g.fft(0); for(int i=0; i<2*n; i++) f[i]*= g[i];
			f.fft(1); for(int i=0; i<n; i++) f[i] = 0;
			f.fft(0); for(int i=0; i<2*n; i++) f[i]*= g[i];
			f.fft(1); for(int i=n; i<2*n; i++) I.push_back(-f[i]);
		}
		I.resize(d); return I;
	}
	modpoly& operator/=(modpoly q){
		reverse(), q.reverse();
		int m = max(0, size()-q.size()+1);
		(*this)*= q.inv(m);
		resize(m), reverse(); return *this;
	}
	friend modpoly operator/(modpoly p, modpoly q){return p/= q;}
	modpoly& operator%=(modpoly q){
		modpoly d = (*this)/q; (*this)-= d*q;
		resize(q.size()-1); return *this;
	}
	friend modpoly operator%(modpoly p, modpoly q){return p%= q;}

	//// LOG, EXP, (TODO) SQRT, (TODO) POW
	modpoly log(int d){return (derivative() * inv(d)).resized(d-1).integral();}
	modpoly exp(int d){
		assert(!empty() && P[0] == (modint)0);
		modpoly Q(1); Q[0] = 1;
		while(Q.size() < d){
			int n = Q.size();
			modpoly M = resized(n*2) - Q.log(n*2); M[0]+= (modint)1;
			Q = M*Q; Q.resize(n*2);
		}
		Q.resize(size()); return Q;
	}

	//// EVAL
	vector<modint> multieval(vector<modint> xs){
		vector<modpoly> tree;
		for(modint x: xs) tree.push_back(modpoly({-x, 1}));
		int i, ti;
		for(i=0; i+1<sz(tree); i+= 2)
			tree.push_back(tree[i] * tree[i+1]);
		tree[i] = *this % tree[i];
		for(ti=i, i--; i>0; i-= 2, ti--){
			tree[i] = tree[ti] % tree[i];
			tree[i-1] = tree[ti] % tree[i-1];
		}
		for(int j=0; j<sz(xs); j++) xs[j] = tree[j][0];
		return xs;
	}
};
