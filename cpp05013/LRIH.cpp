ll LRIH(vector<int>& h){
    h.push_back(0);
    stack<int> S; ll ans=0; size_t i=0;
    while(i < h.size()){
        if(S.empty() || h[S.top()] <= h[i]){S.push(i++); continue;}
        int top = S.top(); S.pop();
        int left = S.empty()? i : (i-S.top()-1);
        ans = max(ans, (ll)h[top]*left);
    }
    return ans;
}