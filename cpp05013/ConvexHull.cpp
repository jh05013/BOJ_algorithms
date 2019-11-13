// Remove rotcal if you don't need it
template <typename T>
struct pnt{
    T x, y;
    pnt(): x{0}, y{0} {}
    pnt(T x, T y): x{x}, y{y} {}
    pnt<T>& operator=(const pnt<T>& b){x = b.x; y = b.y; return *this;}
    bool operator<(const pnt<T>& b){return x<b.x || (x==b.x && y<b.y);}
};
template <typename T>
T ccw(const pnt<T>& a, const pnt<T>& b, const pnt<T>& c){
    return (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x);
}
template <typename T>
struct Hull{
    vector<pnt<T>> p, U, L;
    void add(T x, T y){p.push_back(pnt<T>(x,y));}
    void make(){
        sort(entire(p));
        for(auto q: p){
            while(U.size() > 1 && ccw(U[U.size()-2], U[U.size()-1], q) >= 0) U.pop_back();
            while(L.size() > 1 && ccw(L[L.size()-2], L[L.size()-1], q) <= 0) L.pop_back();
            U.push_back(q); L.push_back(q);
        }
    }
    vector<pnt<T>> rotcal(){
        vector<pnt<T>> res;
        size_t i = 0, j = L.size()-1;
        while(i < U.size()-1 || j > 0){
            res.push_back(U[i]);
            res.push_back(L[j]);
            if(i == U.size()-1) j--;
            else if(j == 0) i++;
            else if((U[i+1].y-U[i].y)*(L[j].x-L[j-1].x) > 
                (L[j].y-L[j-1].y)*(U[i+1].x-U[i].x)) i++;
            else j--;
        }
        return res;
    }
    int size(){return U.size() + L.size() - 2;}
};