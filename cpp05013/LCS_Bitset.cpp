// https://www.secmem.org/blog/2019/09/12/lcs-with-bitset/
#define GET(arr, x) (((arr[x >> 6] >> (x & 63)) & 1) == 1)
#define SET(arr, x) (arr[x >> 6] |= 1llu << (x & 63))
typedef unsigned long long ull;
int lcs(string A, string B){
    int N = A.size(), M = B.size(), sz = (M>>6)+1;
    vector<vector<ull>> S(256, vector<ull>(sz));
    for(int j=0; j<M; j++) SET(S[B[j]], j);
    vector<ull> row(sz);
    for(int j=0; j<M; j++) if(A[0] == B[j]){SET(row, j); break;}
    for(int i=1; i<N; i++){
        ull shl_carry = 1, minus_carry = 0;
        for(int k=0; k<sz; k++){
            ull x_k = S[A[i]][k] | row[k];
            ull term_1 = (row[k] << 1) | shl_carry;
            shl_carry = row[k] >> 63;
            auto sub_carry = [](ull &x, ull y){
                ull tmp = x; return (x = tmp-y) > tmp;
            };
            ull term_2 = x_k;
            minus_carry = sub_carry(term_2, minus_carry);
            minus_carry += sub_carry(term_2, term_1);
            row[k] = x_k & (x_k ^ term_2);
        }
        row[M >> 6]&= (1llu << (M & 63)) - 1;
    }
    int ret = 0;
    for(int j=0; j<M; j++) if(GET(row, j)) ret++;
    return ret;
}