def rot13(message):
    return ''.join([(chr(ord(c) + ((13 - 26) if ord(c.upper()) > ord('M') else 13))) if (ord('A') <= ord(c.upper()) <= ord('Z')) else c for c in message])
