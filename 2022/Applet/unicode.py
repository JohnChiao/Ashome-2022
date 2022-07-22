MODULE = "unicode"
def encode (text,rule = 'utf-8'):
    'encode'
    print(text.encode(rule))
def decode (byte,rule = 'utf-8'):
    'decode'
    print(byte.decode(rule))
