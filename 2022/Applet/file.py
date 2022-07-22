MODULE = "file"
import os


def dinfo():
	d = os.name
	if d == 'nt':
		print("["+MODULE+"]"+'当前系统：Microsoft Windows(AMD32)')
	else:
		print("["+MODULE+"]"+'当前系统：Apple MacOS')

def dir(obj = os.getcwd()):
	for curDir, dirs, files in os.walk(obj):
		print("["+MODULE+"]"+"====================")
		print("["+MODULE+"]"+"现在的目录：" + curDir)
		print("["+MODULE+"]"+"该目录下包含的子目录：" + str(dirs))
		print("["+MODULE+"]"+"该目录下包含的文件：" + str(files))
	return os.walk(obj)


def formatTime(longtime):
	'''格式化日期时间的函数
	   longtime：要格式化的时间
	'''
	import time  # 导入时间模块
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(longtime))


def formatByte(number):
	'''格式化大小的函数
	   number：要格式化的字节数
	'''    
	for (scale,label) in [(1024*1024*1024,"GB"),(1024*1024,"MB"),(1024,"KB")]:
		if number>= scale:   # 如果文件大小大于等于1KB
			return "%.2f %s" %(number*1.0/scale,label)
		elif number == 1: # 如果文件大小为1字节
			return "1 字节"
		else:   # 处理小于1KB的情况
			byte = "%.2f" % (number or 0) 
	return (byte[:-3] if byte.endswith('.00') else byte)+" 字节"  # 去掉结尾的.00，并且加上单位“字节”


def info(file):
	fileinfo = os.stat(file) # 获取文件的基本信息
	print("["+MODULE+"]"+"文件完整路径：", os.path.abspath(file))
	print("["+MODULE+"]"+"索引号：",fileinfo.st_ino)
	print("["+MODULE+"]"+"设备名：",fileinfo.st_dev)
	print("["+MODULE+"]"+"文件大小：",formatByte(fileinfo.st_size))
	print("["+MODULE+"]"+"最后一次访问时间：",formatTime(fileinfo.st_atime))
	print("["+MODULE+"]"+"最后一次修改时间：",formatTime(fileinfo.st_mtime))
	print("["+MODULE+"]"+"最后一次状态变化时间：",formatTime(fileinfo.st_ctime))



def cd(file):
	os.chdir(file)
	print("["+MODULE+"]"+os.getcwd()+'>')

def md(dirn):
	os.makedirs(dirn)
	print("["+MODULE+"]"+os.getcwd()+'>')

def rd(dirn):
	os.removedirs(dirn)
	print("["+MODULE+"]"+os.getcwd()+'>')

def reset():
	os.chdir(os.getcwd)
	print("["+MODULE+"]"+os.getcwd()+'>')

def ren(dirn):
	os.rename(dirn)
	print("["+MODULE+"]"+os.getcwd()+'>')