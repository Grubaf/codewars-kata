def find_missing_letter(chars):
    return [chr(ord(v) - 1) for k, v in enumerate(chars) if ord(v) - ord(chars[k - 1]) > 1][0]
