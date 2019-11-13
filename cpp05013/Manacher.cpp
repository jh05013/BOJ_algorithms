// Use space to insert space between each character
// To get even length palindromes!

vector<int> manacher(string& s){
    int n = s.size(), R = -1, p = -1;
    vector<int> A(n);
    for(int i=0; i<n; i++){
        if(i <= R) A[i] = min(A[2*p-i], R-i);
        while(i-A[i]-1 >= 0 && i+A[i]+1 < n && s[i-A[i]-1] == s[i+A[i]+1]) A[i]++;
        if(i+A[i] > R) R = i+A[i], p = i;
    }
    return A;
}

string space(string& s){
    string t;
    for(char c: s) t+= c, t+= ' ';
    t.pop_back();
    return t;
}

int maxpalin(vector<int>& M, int i){
    if(i%2) return (M[i]+1)/2*2;
    return M[i]/2*2 + 1;
}