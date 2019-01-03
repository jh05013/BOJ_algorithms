ll modmul(ll a, ll b, ll m){
    return ll((__int128)a * (__int128)b % m);
}

ll pow(ll a, ll x, ll mod){
    a%= mod; ll r;
    for(r=1; x; x/=2){if(x%2) r = modmul(r,a,mod); a = modmul(a,a,mod);}
    return r;
}

typedef unsigned long long ull;
bool witness(ull a, ull n, ull s){
    if(a >= n) a%= n;
    if(a <= 1) return true;
    ull d = n>>s, x = pow(a, d, n);
    if(x == 1 || x == n-1) return true;
    while(s-- > 1){
        x = modmul(x, x, n);
        if(x == 1) return false;
        if(x == n-1) return true;
    }
    return false;
}

bool millerRabin(ull n){
    if(n == 2) return true;
    if(n < 2 || n%2 == 0) return false;
    ull d = n>>1, s = 1;
    for(; (d&1)==0; s++) d>>=1;
#define T(a) witness(a##ull, n, s)
    if(n < 4759123141ull) return T(2) && T(7) && T(61);
    return T(2) && T(325) && T(9375) && T(28178)
        && T(450775) && T(9780504) && T(1795265022);
#undef T
}

ll rho(ll n){
    random_device rd; mt19937 gen(rd());
    uniform_int_distribution<ll> dis(1, n-1);
    ll x = dis(gen), c = dis(gen), g = 1; ll y = x;
    while(g == 1){
        x = (modmul(x, x, n) + c) % n;
        y = (modmul(y, y, n) + c) % n;
        y = (modmul(y, y, n) + c) % n;
        g = __gcd(abs(x-y), n);
    }
    return g;
}

void factorize(ll n, vector<ll>& fl){
    if(n == 1) return;
    if(n%2 == 0) fl.push_back(2), factorize(n/2, fl);
    else if(millerRabin(n)) fl.push_back(n);
    else{
        ll f = rho(n);
        factorize(f, fl); factorize(n/f, fl);
    }
}