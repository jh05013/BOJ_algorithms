const int MOD = 1000000007;
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