# LCS: Longest common subsequence (length version)
# LCS_s: Longest common subsequence (sequence version)
# a, b = two sequences

def LCS(a, b):
    lcs = [[0]*(len(b)+1) for i in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]: lcs[i][j] = lcs[i-1][j-1]+1
            else: lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    return lcs[-1][-1]

def LCS_s(a, b):
    lcs = [[0]*(len(b)+1) for i in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]: lcs[i][j] = lcs[i-1][j-1]+1
            else: lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    track = ''
    i-= 1; j-= 1
    while i>=0 and j>=0:
        if a[i]==b[j]: track+= a[i]; i-= 1; j-= 1
        elif lcs[i+1][j] > lcs[i][j+1]: j-= 1
        else: i-= 1
    print(track[::-1])