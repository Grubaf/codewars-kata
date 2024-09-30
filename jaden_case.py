def to_jaden_case(string):
    return ' '.join(map(lambda s: s[0].upper() + s[1:].lower(), string.split(' ')))
