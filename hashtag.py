def generate_hashtag(s):
    res = '#' + ''.join([w.capitalize() for w in s.split()])
    return res if 1 < len(res) <= 140 else False
