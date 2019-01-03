// Failure function
vector<int> fail(string& w){
    vector<int> T(w.size());
    for(size_t i=1, j=0; i < w.size(); i++){
        while(j && w[i] != w[j]) j = T[j-1];
        if(w[i] == w[j]) T[i] = ++j;
    }
    return T;
}

// Find w in s: return first index, -1 if none
int kmp(string& s, string& w, vector<int>& T){
    int m = 0, i = 0;
    while(m+i < (int)s.size()){
        if(w[i] == s[m+i]){if(i++ == (int)w.size()-1) return m;}
        else if(i) m = m+i-T[i], i = T[i];
        else m++, i = 0;
    }
    return -1;
}

// Find w in s but without precomputing failure
int kmp(string& s, string& w){
    vector<int> T(w.size());
    for(size_t i=1, j=0; i < w.size(); i++){
        while(j && w[i] != w[j]) j = T[j-1];
        if(w[i] == w[j]) T[i] = ++j;
    }
    int m = 0, i = 0;
    while(m+i < (int)s.size()){
        if(w[i] == s[m+i]){if(i++ == (int)w.size()-1) return m;}
        else if(i) m = m+i-T[i], i = T[i];
        else m++, i = 0;
    }
    return -1;
}

// Find w in s: return the vector of indices
vector<int> kmp(string& s, string& w, vector<int>& T){
    int m = 0, i = 0;
    vector<int> res;
    while(m+i < (int)s.size()){
        if(w[i] == s[m+i]){if(i++ == (int)w.size()-1) res.push_back(m);}
        else if(i) m = m+i-T[i-1], i = T[i-1];
        else m++, i = 0;
    }
    return res;
}

// Find w in s but without precomputing failure
vector<int> kmp(string& s, string& w){
    vector<int> T(w.size());
    for(size_t i=1, j=0; i < w.size(); i++){
        while(j && w[i] != w[j]) j = T[j-1];
        if(w[i] == w[j]) T[i] = ++j;
    }
    int m = 0, i = 0;
    vector<int> res;
    while(m+i < (int)s.size()){
        if(w[i] == s[m+i]){if(i++ == (int)w.size()-1) res.push_back(m);}
        else if(i) m = m+i-T[i-1], i = T[i-1];
        else m++, i = 0;
    }
    return res;
}