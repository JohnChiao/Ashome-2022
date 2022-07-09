import os


def devinfo():
    dev = os.name
    if dev == 'nt':
        print('当前系统：Microsoft Windows(AMD32)')
    else:
        print('当前系统：Apple MacOS')

def dir(obj = os.getcwd()):
    for curDir, dirs, files in os.walk(obj):
        print("====================")
        print("现在的目录：" + curDir)
        print("该目录下包含的子目录：" + str(dirs))
        print("该目录下包含的文件：" + str(files))

def info(file):
    '''file:绝对路径'''
    fileinfo = os.stat(file)
    print('索引号：',fileinfo.st_ino)
    print('大小：',fileinfo.st_size,'字节')

def cd(file):
    os.chdir(file)
    print(os.getcwd()+'>')

def md(dirn):
    os.makedirs(dirn)
    print(os.getcwd()+'>')

def rd(dirn):
    os.removedirs(dirn)
    print(os.getcwd()+'>')

def reset():
    os.chdir(os.getcwd)
    print(os.getcwd()+'>')

def ren(dirn):
def ren(dirn):
    os.rename(dirn)
    print(os.getcwd()+'>')