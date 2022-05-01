#define TTT template <typename T>
#define FR friend
const double pi = 3.14159265358979323846264338327950288;
TTT int sgn(T x){return (T(0)<x) - (x<T(0));}
TTT T sq(T x){return x*x;}

////// Point //////

const int PNT_UNINIT = -666;
TTT struct Pnt{
    T x, y; int idx;
	Pnt(T X=0, T Y=0, int I=PNT_UNINIT): x(X), y(Y), idx(I) {}
#define CSP const Pnt&
	// io
	FR istream& operator>>(istream& is, Pnt& p){return is>>p.x>>p.y;}
	FR ostream& operator<<(ostream& os, CSP p){return os<<"("<<p.x<<", "<<p.y<<")";}

	// basic
	Pnt operator-() const {return {-x, -y};}
	Pnt& operator+=(CSP q){x+= q.x, y+= q.y; return *this;}
	Pnt& operator-=(CSP q){x-= q.x, y-= q.y; return *this;}
	Pnt& operator*=(T k){x*= k, y*= k; return *this;}
	Pnt& operator/=(T k){x/= k, y/= k; return *this;}
	FR Pnt operator+(Pnt p, CSP q){return p+=q;}
	FR Pnt operator-(Pnt p, CSP q){return p-=q;}
	FR Pnt operator*(Pnt p, T k){return p*=k;}
	FR Pnt operator*(T k, Pnt p){return p*=k;}
	FR Pnt operator/(Pnt p, T k){return p/=k;}
	FR bool operator==(CSP a, CSP b){return a.x==b.x && a.y==b.y;}
	FR bool operator!=(CSP a, CSP b){return !(a==b);}
	FR bool operator<(CSP a, CSP b){return a.x<b.x || (a.x==b.x && a.y<b.y);}
	FR bool operator>(CSP a, CSP b){return b<a;}
	FR bool operator<=(CSP a, CSP b){return a.x<b.x || (a.x==b.x && a.y<=b.y);}
	FR bool operator>=(CSP a, CSP b){return b<=a;}
	FR T dot(CSP p, CSP q){return p.x*q.x + p.y*q.y;}
	FR T cross(CSP p, CSP q){return p.x*q.y - p.y*q.x;}

	// distance
	FR T sq(CSP p){return p.x*p.x + p.y*p.y;}
	FR double abs(CSP p){return sqrt(sq(p));}
	FR T distsq(CSP p, CSP q){return sq(p-q);}
	FR double dist(CSP p, CSP q){return sqrt(distsq(p, q));}

	// angle
	FR bool is_perp(CSP p, CSP q){return dot(p, q)==0;}
	FR double angle(CSP p, CSP q){
		return acos(clamp(dot(p,q) / abs(p) / abs(q), -1.0, 1.0));
	}
	FR double angle(CSP c, CSP p, CSP q){return angle(p-c, q-c);}
	FR double angle_ccw(CSP p, CSP q){
		double theta = angle(p, q);
		return orient(p, Pnt<T>(0,0), q) <= 0? theta : 2*pi - theta;
	}
	FR double angle_ccw(CSP c, CSP p, CSP q){return angle_ccw(p-c, q-c);}

	// orientation (<0 cw, =0 collinear, >0 ccw)
	FR T orient(CSP p, CSP q, CSP r){return cross(q-p, r-p);}
	FR int ccw(CSP p, CSP q, CSP r){return sgn(orient(p, q, r));}

	// transformation
	FR Pnt scale(CSP c, CSP p, T factor){return c + (p-c)*factor;}
	FR Pnt rot90(CSP p){return {-p.y, p.x};}
	FR Pnt rot90(CSP c, CSP p){return c + rot90(p-c);}
	/* TODO: FLOAT
	FR Pnt rot(CSP p, double theta){
		double c = cos(theta), s = sin(theta);
		return {p.x*c - p.y*s, p.x*s + p.y*c};
	}
	FR Pnt rot(CSP c, CSP p, double theta){return c + rot(p-c, theta);} */
#undef CSP
};