import easygui
print("Imported",easygui)
import gc
print("Imported",gc)
import getpass
print("Imported",getpass)
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
import sqlite3
print("Imported",sqlite3)
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



class User:
	def __init__(self, name):
		User.activaty = self
		self.name = name
	def logout(self):
		User.activaty = None
		return 0


def envvar():
	return print(locals())


print("Initializing users...")
import sqlite3
def create_sql():
	sql = sqlite3.connect("userdata.ini")
	sql.execute("""create table if not exists
		user(
		id integer primary key autoincrement,
		name varchar(128),
		password varchar(128))
		""")

	sql.close()
create_sql()
 
def showdata(username):
	sql = sqlite3.connect('userdata.ini')
	data = sql.execute("select * from user where name='%s'" % username).fetchone()
	sql.close()
	return data

def login():
	name = input("Enter username:")
	data = showdata(name)
	if data:
		password = getpass.getpass("Enter password:")
		if data[2] == password:
			user = User(name)
		else:
			print("Password is wrong!")
			quit()
	else:
		print("Username not found")
		quit()


def signup():
	input_name = input("Enter username:")
	input_password = getpass.getpass("Setup password:")
	sql = sqlite3.connect("userdata.ini")
	sql.execute("insert into user(name,password) values(?,?)",
				(input_name,input_password))
	sql.commit()
	user = User(input_name)
	sql.close()

