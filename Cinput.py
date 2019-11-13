XRAW = __import__('sys').stdin.read().split()
XIN = iter(XRAW)
O = lambda: int(next(XIN))