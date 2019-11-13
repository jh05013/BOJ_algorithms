// pll version

typedef pair<ll,ll> pll;

// positive -> ccw; negative -> cw; 0 -> collinear
ll ccw(pll a, pll b, pll c){
    auto [ax,ay] = a; auto [bx,by] = b; auto [cx,cy] = c;
    return (bx-ax)*(cy-ay) - (by-ay)*(cx-ax);
}

// struct version

struct point{
    ll x, y;
    point(ll x, ll y): x{x}, y{y} {}
};

// positive -> ccw; negative -> cw; 0 -> collinear
ll ccw(point a, point b, point c){
    return (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x);
}