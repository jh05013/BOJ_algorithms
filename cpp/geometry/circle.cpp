////// Circle //////
// DEPENDENCY: POINT

TTT struct Circle{
	Pnt<T> cent; T r = 0;
	Circle(Pnt<T> C=Pnt<T>(), T R=0): cent(C), r(R) {}
#define FR friend
#define CSP const Circle&
	// io
	FR istream& operator>>(istream& is, Circle& c){return is>>c.cent>>c.r;}
	FR ostream& operator<<(ostream& os, CSP c){return os<<"¡Ü"<<c.cent<<"+"<<c.r;}

	// interior check
	FR bool contains(CSP c, Pnt<T> p, bool strict=false){
		T d1 = distsq(p, c.cent), d2 = sq(c.r);
		return strict? d1<d2 : d1<=d2;
	}
	FR bool contains(CSP C, CSP c, bool strict=false){
		if(C.r < c.r) return false;
		T d1 = distsq(C.cent, c.cent), d2 = sq(C.r - c.r);
		return strict? d1<d2 : d1<=d2;
	}
	// TODO line segment

	// TODO intersection check

	FR bool disjoint_interior(CSP C, CSP c, bool strict=false){
		T d1 = sq(C.r + c.r), d2 = distsq(C.cent, c.cent);
		return strict? d1<d2 : d1<=d2;
	}
	// TODO line segment
};