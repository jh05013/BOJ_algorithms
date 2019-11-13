#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin>>n;
    vector<int> dp = {3, 2};

    cout << dp[0] << ',';
    for(int i=2; i<=n; i++){
        vector<int> ndp(1<<i, 0x3f3f3f3f);
        int BIT = 1<<(i-1);
        for(int a=0; a<BIT; a++) for(int b=0; b<BIT; b++){
            // largest disc inverted
            ndp[a^b^BIT] = min(ndp[a^b^BIT], dp[a]+dp[b]+2);
            // largest disc not inverted
            for(int c=0; c<BIT; c++){
                ndp[a^b^c] = min(ndp[a^b^c], dp[a]+dp[b]+dp[c]+4);
            }
        }
        dp = ndp;
        cout << dp[0] << ',';
    }
}