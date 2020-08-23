import base64, zlib
def encipher(s): return base64.b85encode(zlib.compress(s.encode('utf-8')))
def decipher(s): return zlib.decompress(base64.b85decode(s)).decode('utf-8')