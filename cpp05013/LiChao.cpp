// This tree finds maximum.
// Make sure |a||x|+|b| <= INF.

const ll INF = 0x3f3f3f3f3f3f3f3f;
struct Line{
    ll a, b;
    ll operator()(ll x){return a*x+b;}
};
struct Node{
    int left, right; ll xl, xr;
    Line l;
};

struct Lichao{
    vector<Node> nodes;
    Lichao(ll xmin, ll xmax){
        nodes.push_back({-1,-1, xmin,xmax, {0,-INF}});
    }
    void insert(ll a, ll b){return insert(0, {a,b});}
    ll get(ll x){return get(0, x);}

    void insert(int n, Line newline){
        ll xl = nodes[n].xl, xr = nodes[n].xr, xm = (xl+xr)>>1;
        Line llo = nodes[n].l, lhi = newline;
        if(llo(xl) > lhi(xl)) swap(llo, lhi);
        if(llo(xr) <= lhi(xr)){nodes[n].l = lhi; return;}
        else if(llo(xm) < lhi(xm)){
            nodes[n].l = lhi;
            if(nodes[n].right == -1){
                nodes[n].right = nodes.size();
                nodes.push_back({-1,-1, xm+1,xr, {0,-INF}});
            }
            insert(nodes[n].right, llo);
        }
        else{
            nodes[n].l = llo;
            if(nodes[n].left == -1){
                nodes[n].left = nodes.size();
                nodes.push_back({-1,-1, xl,xm, {0,-INF}});
            }
            insert(nodes[n].left, lhi);
        }
    }
    ll get(int n, ll x){
        if(n == -1) return -INF;
        ll xl = nodes[n].xl, xr = nodes[n].xr, xm = (xl+xr)>>1;
        int m = (x <= xm)? nodes[n].left : nodes[n].right;
        return max(nodes[n].l(x), get(m, x));
    }
};