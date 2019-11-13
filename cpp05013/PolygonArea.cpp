typedef pair<ll,ll> pll;
// returns TWICE the area
ll area(vector<pll> &P){
    ll ans = 0;
    P.push_back(P[0]);
    for(int i=0; i<P.size()-1; i++)
        ans+= P[i].first*P[i+1].second - P[i+1].first*P[i].second;
    P.pop_back();
    return ans;
}