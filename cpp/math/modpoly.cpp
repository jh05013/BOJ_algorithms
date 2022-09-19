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

	//// INIT & basic
	modpoly(int n): P(n) {}
	modpoly(vector<modint> A): P(A) {}
	modint& operator[](int i){return P[i];}
	int size(){return sz(P);}
	void resize(int n){P.resize(n);}

	//// IO
	friend istream& operator>>(istream &is, modpoly &p){
		for(int i=0; i<p.size(); i++) is>>p[i];
		return is;
	}
	friend ostream& operator<<(ostream &os, const modpoly &p){
		for(modint x:p.P) os<<x<<' ';
		return os;
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
};
