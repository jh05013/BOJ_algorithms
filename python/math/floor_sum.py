# computes sum((a*i+b)//m for i in range(n)) in O(log m)
# 0 <= n; 1 <= m
def floor_sum(n, m, a, b):
    assert 0 <= n and 1 <= m
    ans = 0
    if a >= m or a < 0: ans+= (n-1)*n//2 * (a//m); a%= m
    if b >= m or b < 0: ans+= n * (b//m); b%= m
    if a == 0: return ans
    y, z = divmod(a*n+b, m)
    return ans + floor_sum(y, a, m, z)

