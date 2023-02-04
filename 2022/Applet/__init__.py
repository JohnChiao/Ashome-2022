import easygui
print("Imported",easygui)
import gc
print("Imported",gc)
import math
print("Imported",math)
import operator
print("Imported",operator)
import os
print("Imported",os)
import random
print("Imported",random)
import re
print("Imported",re)
import shutil
print("Imported",shutil)
import socket
print("Imported",socket)
import string
print("Imported",string)
import sys
print("Imported",sys)
import threading
print("Imported",threading)
import time
print("Imported",time)
import tkinter
print("Imported",tkinter)
import turtle
print("Imported",turtle)
import wave
print("Imported",wave)
import zipfile
print("Imported",zipfile)
# Customize packages
sys.path.append("./Applet")
sys.path.append("./Pack")
from cld import *
from calc import *
from db import *
from file import *
from get import *
from unicode import *
from vi import *
USERID = 0
USERS = []
_PASSWD = {}
userfile = open("profile.ini","a+")
userfiler = open("profile.ini","r")


class User:
	def __init__(self, name, passwd = ""):
		global USERID
		if name not in USERS:
			self.id = USERID
			User.activaty = self
			self.name = name
			USERID += 1
			USERS.append(self.name)
			self.history = ""
			_PASSWD[name] = passwd
			userfile.write(self.name+"\n"+passwd+"\n")
			userfile.flush()
		elif passwd == _PASSWD[name]:
			self.name = name
			self.id = USERS.index(self.name)
			User.activaty = self
		else:
			raise ConnectionError("Password is wrong!")

	def logout(self):
		User.activaty = None
		return 0


def envvar():
	return print(locals())


print("Initializing users...")
USERS = userfiler.readlines()[0::2]
_PASSWD = dict(zip(USERS, userfiler.readlines()[1::2]))