XRAW = __import__('sys').stdin.read().split()
XIN = iter(XRAW)
input = lambda: next(XIN)