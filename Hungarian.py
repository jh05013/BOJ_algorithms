# Hungarian algorithm in O(MNN) for minimum weighted bipartite matching
# http://e-maxx.ru/algo/assignment_hungary

def hungarian(mat):
    def Q(n, val=0): return [val]*(n+1)
    n = len(mat); m = len(mat[0])
    u = Q(n); v=Q(m); p=Q(m); way=Q(m)
    for i in range(1, n+1):
        p[0] = i; j0 = 0; minv = Q(m, float('inf')); used = Q(m, False);
        while p[j0]:
            used[j0] = True; i0 = p[j0]; delta = float('inf'); j1 = None
            for j in range(1, m+1):
                if used[j]: continue
                cur = mat[i0-1][j-1] - u[i0] - v[j]
                if cur < minv[j]: minv[j] = cur; way[j] = j0
                if minv[j] < delta: delta = minv[j]; j1 = j
            for j in range(m+1):
                if used[j]: u[p[j]]+= delta; v[j]-= delta
                else: minv[j]-= delta
            j0 = j1
        while j0: j1 = way[j0]; p[j0] = p[j1]; j0 = j1
    return -v[0]