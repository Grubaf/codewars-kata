def unique_in_order(sequence):
    last = None
    xd = []
    
    for s in sequence:
        if s != last:
            last = s
            xd.append(s)
    
    return xd
