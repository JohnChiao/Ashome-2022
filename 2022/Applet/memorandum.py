def init ():
    global memorandum
    memorandum = 'Value{NULL}'
    print('BackValue:in{memorandum.init}')
def set (value='Value{NULL}'):
    global memorandum
    memorandum = value
    print('memorandum:',memorandum)
def view ():
    print('memorandum:',memorandum)
