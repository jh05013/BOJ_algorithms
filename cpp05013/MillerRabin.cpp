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