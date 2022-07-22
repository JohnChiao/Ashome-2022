MODULE = "memorandum"
def init ():
    global memorandum
    memorandum = 'Value{NULL}'
    print("["+MODULE+"]"+'BackValue:in{memorandum.init}')
def set (value='Value{NULL}'):
    global memorandum
    memorandum = value
    print("["+MODULE+"]"+'memorandum:',memorandum)
def view ():
    print("["+MODULE+"]"+'memorandum:',memorandum)
