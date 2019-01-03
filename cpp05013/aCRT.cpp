pair<ll, ll> egcd(ll a, ll b){
    if(b == 0) return {1, 0};
    auto t = egcd(b, a%b);
    return {t.second, t.first-t.second*(a/b)};
}

ll modinv(ll a, ll m){return (egcd(a,m).first%m + m)%m;}

ll CRT(vector<ll> &a, vector<ll> &n, int pt = 0){
    if(pt == a.size()-1) return a[pt];
    ll a0 = a[pt], a1 = a[pt+1], n0 = n[pt], n1 = n[pt+1];
    ll tmp = modinv(n0, n1);
    ll tmp2 = (tmp*(a1-a0) % n1 + n1) % n1;
    ll ora = a1, tgcd = __gcd(n0, n1);
    a[pt+1] = a0 + n0/tgcd*tmp2;
    n[pt+1]*= n0/tgcd;
    ll ret = CRT(a, n, pt+1);
    n[pt+1]/= n0/tgcd;
    a[pt+1] = ora;
    return ret;
}