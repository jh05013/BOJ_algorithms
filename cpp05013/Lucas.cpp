ll pow(ll a, ll x, ll mod){
    a%= mod; ll r;
    for(r=1; x; x/=2){if(x%2) r = r*a%mod; a = a*a%mod;}
    return r;
}

ll nck(ll n, ll k, ll m){
    if(n < k) return 0;
    ll res = 1;
    for(int i=0; i<k; i++){
        res = res*(n-i) % m;
        res = res*pow(i+1, m-2, m) % m;
    }
    return res;
}

ll lucas(ll n, ll k, ll m){
    ll res = 1;
    while(n || k){
        res = res*nck(n%m, k%m, m) % m;
        n/= m, k/= m;
    }
    return res;
}