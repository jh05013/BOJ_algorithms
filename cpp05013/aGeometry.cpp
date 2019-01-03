template <typename T>
struct pnt{
    T x, y;
    pnt(T x, T y): x{x}, y{y} {}
};



// ccw check
// positive -> ccw; negative -> cw; 0 -> collinear
template <typename T>
struct pnt{
    T x, y;
    pnt(T x, T y): x{x}, y{y} {}
};
template <typename T>
T ccw(pnt<T> a, pnt<T> b, pnt<T> c){
    return (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x);
}



// twice the polygon area (so that it returns T)
template <typename T>
struct pnt{
    T x, y;
    pnt(T x, T y): x{x}, y{y} {}
};
template <typename T>
T area2(vector<pnt<T>> &p){
    p.push_back(p[0]);
    T res = 0;
    for(size_t i=0; i<p.size()-1; i++)
        res+= p[i].x*p[i+1].y - p[i+1].x*p[i].y;
    p.pop_back();
    return abs(res);
}



// line intersection check
template <typename T>
struct pnt{
    T x, y;
    pnt(T x, T y): x{x}, y{y} {}
    bool operator=(pnt<T> b){return x==b.x && y==b.y;}
};
template <typename T>
T ccw(pnt<T> a, pnt<T> b, pnt<T> c){
    return (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x);
}
T cc(pnt<T> a, pnt<T> b, pnt<T> c){
    return min(a.x,b.x) <= c.x && c.x <= max(a.x,b.x) &&
           min(a.y,b.y) <= c.y && c.y <= max(a.y,b.y);
}
bool intersect(pnt<T> a, pnt<T> b, pnt<T> c, pnt<T> d){
    if(a == b) return a == c || a == d;
    if(c == d) return c == a || c == b;
    T s1 = ccw(a,b,c), s2 = ccw(a,b,d);
    if(s1 == 0 && s2 == 0)
        return cc(a,b,c) || cc(a,b,d) || cc(c,d,a) || cc(c,d,b);
    if(s1 && s1 == s2) return false;
    s1 = ccw(c,d,a), s2 = ccw(c,d,b);
    return !s1 || s1 != s2;
}