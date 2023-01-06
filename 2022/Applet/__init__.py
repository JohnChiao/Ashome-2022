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
from cld import *
from calc import *
from db import *
from file import *
from get import *
from unicode import *
from vi import *
_USERID = -1


class User:
	def __init__(self, name):
		global _USERID
		self.name = name
		self.id = _USERID
		_USERID += 1
		self.history = ""
		User.activaty = self
		self.pkg = PackSystem()

	def logout(self):
		User.activaty = None
		return 0
	

class PackSystem(User):
	def __init__(self):
		self.pkglist = next(os.walk("./Pack"))[1]

	def uninstall(self):
		if self.strlist:
			choice = easygui.choicebox("Uninstall:", "Pachage Manager", self.pkglist)
			if choice and choice in self.pkglist:
				del choice
				self.pkglist.remove(choice)
		else:
			easygui.msgbox("No package!", "Package Manager")

	def __call__(self):
		while True:
			self.strlist = "\n".join(self.pkglist)
			choice = easygui.buttonbox(self.strlist if self.strlist else "No package", "Package Manager", ["Uninstall Package", "Quit"])
			if choice == "Uninstall Package":
				self.uninstall()
			else:
				break

print("Initializing user...")
SYSTEM = User("SYSTEM")