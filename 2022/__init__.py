from email.mime import image
import platform
from run import *
import os
import sys
import re
import setup
import getpass
import easygui
VERSION = "2022.10.5"
code = ""
_ca = open("__pycache__/log.txt",mode='w')
_ca.close()
del _ca


def main():
	code = "Undefined"
	while True:
		pwd = os.getcwd()
		code = input(User.activaty.name+" @ "+platform.system()+" : "+pwd+">")
		if code == "-q":
			shutdown()
		elif code == "..":
			os.chdir("..")
		elif code == ".":
			os.chdir(".")
		elif code == "cd":
			file.cd(easygui.diropenbox("Choice directory:","cd"))
		elif code == "~":
			file.cd(os.path.expanduser('~'))
		elif code == "-h":
			help()
		elif "-i" in code:
			exec("import "+code[3:])
		else:
			try:
				exec("print("+User.activaty.history+")" if code == "-h" else "print("+code+")")
				if User.activaty == None:
					admin = User(easygui.enterbox("Input new username:","Logout"))
					main()
				User.activaty.history = User.activaty.history if code == "-h" else code
				User.activaty.cachefile.write("Run:\n\tCode:\n\t\t"+User.activaty.history+"\n")
				User.activaty.cachefile.flush()
			except KeyboardInterrupt:
				shutdown()
			except NameError as err:
				print("NameError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
				if easygui.boolbox("If something went wrong, press <Debug> to debug","Oops!",("[D]ebug","[I]gnore")):
					input("[DEBUGING]Press <enter> to end debug")
				User.activaty.cachefile.write("NameError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
				User.activaty.cachefile.flush()
			except TypeError as err:
				print("TypeError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
				if easygui.boolbox("If something went wrong, press <Debug> to debug","Oops!",("[D]ebug","[I]gnore")):
					input("[DEBUGING]Press <enter> to end debug")
				User.activaty.cachefile.write("TypeError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
				User.activaty.cachefile.flush()
			except IOError as err:
				print("IOError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
				User.activaty.cachefile.write("IOError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
				User.activaty.cachefile.flush()
			except KeyError as err:
				print("KeyError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
				if easygui.boolbox("If something went wrong, press <Debug> to debug","Oops!",("[D]ebug","[I]gnore")):
					input("[DEBUGING]Press <enter> to end debug")
				User.activaty.cachefile.write("KeyError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
				User.activaty.cachefile.flush()
			except ValueError as err:
				print("ValueError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
				if easygui.boolbox("If something went wrong, press <Debug> to debug","Oops!",("[D]ebug","[I]gnore")):
					input("[DEBUGING]Press <enter> to end debug")
				User.activaty.cachefile.write("ValueError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
				User.activaty.cachefile.flush()
			except AttributeError as err:
				print("AttributeError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
				if easygui.boolbox("If something went wrong, press <Debug> to debug","Oops!",("[D]ebug","[I]gnore")):
					input("[DEBUGING]Press <enter> to end debug")
				User.activaty.cachefile.write("AttributeError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
				User.activaty.cachefile.flush()


def shutdown():
	if easygui.boolbox("Do you want to exit?","Exit"):
		User.activaty.logout()
		quit()
	else:
		main()


if __name__ == "__main__":
	username = getpass.getuser()
	admin = User(name = username if username else "Admin")
	print("Ashome V"+VERSION)
	print("Environment Version:",platform.python_version())
	main()