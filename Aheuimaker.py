# 한글 -> 초성, 중성, 종성
def destroy(c):
    head = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
    vowel = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
    tail = "ㅗㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"
    o = ord(c) - 44032
    h = head[o // 588]
    o%= 588
    v = vowel[o // 28]
    t = tail[o % 28]
    if t == "ㅗ": t = ""
    return h, v, t

# 초성, 중성, 종성 -> 한글
def combine(h, v, t):
    head = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
    vowel = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
    tail = "ㅗㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"
    
    h = head.find(h)
    v = vowel.find(v)
    last = t
    t = tail.find(last) if last else 0
    return chr(44032 + 588*h + 28*v + t)

# 한글 -> 방향 전환 (udlr)
def change_dir(c, d):
    h, v, t = destroy(c)
    if d == 'u': v = 'ㅗ'
    elif d == 'd': v = 'ㅜ'
    elif d == 'l': v = 'ㅓ'
    else: v = 'ㅏ'
    return combine(h, v, t)

tailgen = "..ㄱㄷㅁㄵㅄㄺㅀㄿ"

def make_9(n, base=9):
    T = []
    while n:
        T.append(n%base)
        n//= base
    return T[::-1]

def make_n(n, base):
    # bonus cases
    if n == 32: return '밥밣따맣'
    
    s = ''
    T = make_9(n, base)
    mul = combine('ㅂ', 'ㅏ', tailgen[base])
    
    if T[0] == 1: s+= mul
    else: s+= combine('ㅂ', 'ㅏ', tailgen[T[0]]) + mul + '따'
    for i in range(1, len(T)):
        c = T[i]
        if c == 0: s+= ''
        elif c == 1: s+= '받반타다'
        else: s+= combine('ㅂ', 'ㅏ', tailgen[c]) + '다'
        if i != len(T)-1: s+= mul + '따'
    return s + '맣'

def make_n_opt(n):
    return min([make_n(n, base) for base in range(2, 10)], key=len)

def ordize(s):
    return [ord(c) for c in s]

def aheuize(s):
    return ''.join(make_n_opt(ord(c)) for c in s)

print(aheuize(input()) + '희')