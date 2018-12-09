import base64, zlib
grid = open('gen10.out').readlines()[94:]

s = ''
for row in grid:
    for word in row.split():
        if word == '0' or word == '1': s+= word
assert len(s) == 70*71*141//3
s+= '00'

match = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#"
t = ''
for i in range(0, len(s), 6): t+= match[int(s[i:i+6], 2)]
q = base64.b85encode(zlib.compress(t.encode('utf-8')))