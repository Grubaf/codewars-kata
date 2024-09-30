import math

def persistence(n, c=0):
    return c if n < 10 else persistence(math.prod([int(c) for c in str(n)]), c + 1)
