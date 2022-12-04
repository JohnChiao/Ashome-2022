import easygui
import gc
import math
import operator
import os
import random
import re
import shutil
import socket
import string
import sys
import threading
import time
import tkinter
import turtle
import wave
import zipfile
# Customize packages
sys.path.append("./Applet")
sys.path.append("./Pack")
from calander import *
from compute import *
from db import *
from file import *
from get import *
from unicode import *
from vi import *


class User:
	def __init__(self, name):
		self.name = name
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