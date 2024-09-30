import math

def expanded_form(n):
    s = []
    c = 0
    
    while n >= 1:
        x = math.floor(n % 10) * 10 ** c
        if x != 0:
            s.append(str(x))
        n /= 10
        c += 1
        
    return ' + '.join(reversed(s))
