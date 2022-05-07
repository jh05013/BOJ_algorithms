TTT struct Linear{
	T a, b; // ax+b
	Linear(): a(0), b(0) {}
	Linear(T B): a(0), b(B) {}
	Linear(T A, T B): a(A), b(B) {}

	friend istream& operator>>(istream& is, Linear& f){
		return is >> f.a >> f.b;
	}
	friend ostream& operator<<(ostream& os, const Linear& f){
		if(f.a.val == 0) return os<<f.b;
		if(f.a.val != 1) os<<f.a;
		os<<"x";
		if(f.b.val == 0) return os;
		if(f.b.val > 0) os<<"+";
		return os<<f.b;
	}
	friend bool operator==(const Linear& f, const Linear& g){return f.a==g.a && f.b==g.b;}
	friend bool operator!=(const Linear& f, const Linear& g){return !(f==g);}

	T operator()(const T& x) const {return a*x+b;}
	Linear operator-() const {return Linear(-a, -b);}
	Linear& operator+=(const Linear& m){a+=m.a; b+=m.b; return *this;}
	Linear& operator-=(const Linear& m){a-=m.a; b-=m.b; return *this;}
	Linear& operator*=(const Linear& m){
		a = a*m.b + b*m.a; b = b * m.b;
		return *this;
	}

	friend Linear inv(const Linear& f){
		T ib = T(1)/f.b;
		return Linear(-f.a*ib*ib, ib);
	}
	Linear& operator/=(const Linear& m){return (*this)*= inv(m);}

	friend Linear operator+(Linear f, const Linear& g){return f+= g;}
	friend Linear operator-(Linear f, const Linear& g){return f-= g;}
	friend Linear operator*(Linear f, const Linear& g){return f*= g;}
	friend Linear operator/(Linear f, const Linear& g){return f/= g;}

	friend Linear composite(const Linear& f, const Linear& g){
		return Linear(f.a*g.a, f.a*g.b+f.b);
	} // f(g(x))
};
