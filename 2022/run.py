import zipfile
import wave
import turtle
import tkinter
import time
import threading
import sys
import string
import socket
import shutil
import re
import random
import os
import operator
import math
import gc
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
		self.cachefile = open("__pycache__/"+self.name+"_log.txt",mode='a+')
		self.cachefile.write("============Startup============")

	def logout(self):
		User.activaty = None
		return 0
	