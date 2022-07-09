﻿import zipfile
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
import calander
import compute as calc
import file
import memorandum
import unicode
import vi
import web


class User:
	def __init__(self, name):
		self.name = name
		self.history = ""
		User.activaty = self

	def logout(self):
		User.activaty = None
		return 0

MODULES = (
	zipfile,
	wave,
	turtle,
	tkinter,
	time,
	threading,
	sys,
	string,
	socket,
	shutil,
	re,
	random,
	os,
	operator,
	math,
	gc,
	calander,
	calc,
	file,
	memorandum,
	unicode,
	web
	)
