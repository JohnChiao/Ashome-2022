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
_USERID = 0
USERS = []


class User:
	def __init__(self, name):
		global _USERID
		self.name = name
		if self.name not in USERS:
			self.id = _USERID
			_USERID += 1
			USERS.append(self.name)
			self.history = ""
		else:
			self.id = USERS.index(self.name)
		User.activaty = self

	def logout(self):
		User.activaty = None
		return 0


def envvar():
	return print(locals())


print("Initializing user...")
SYSTEM = User("SYSTEM")