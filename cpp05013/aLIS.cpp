int LIS(vector<int>& L){
    vector<int> best;
    for(int x:L){
        auto it = lower_bound(entire(best), x);
        if(it == best.end()) best.push_back(x);
        else *it = x;
    }
    return best.size();
}

vector<int> LISFind(vector<int>& L){
    vector<int> best, ind, prev, res;
    for(size_t i=0; i<L.size(); i++){
        int x = L[i];
        auto it = lower_bound(entire(best), x);
        int pos = it - best.begin();
        if(it == best.end()) best.push_back(x), ind.push_back(i);
        else *it = x, ind[pos] = i;
        prev.push_back(pos == 0? -1 : ind[pos-1]);
    }
    int k = ind.back();
    while(k != -1){
        res.push_back(L[k]);
        k=prev[k];
    }
    reverse(entire(res));
    return res;
}