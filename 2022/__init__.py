from distutils.log import debug
import platform
from run import *
from pyop import *
import os
import sys
import re
import setup
import getpass
import easygui
# Global Define Start
VERSION = "2022.10.5"
code = ""
_ca = open("__pycache__/log.txt",mode='w')
_ca.close()
del _ca
_prompt = {"nt" : " > ", "posix" : " $ "}
cter = False
# Global Defile Stop
# Login
username = getpass.getuser()
admin = User(name = username if username else "Admin")


def main(ctr = cter):
	code = "Undefined"

	while True:
		pwd = os.getcwd()
		code = input((User.activaty.name+" @ "+platform.system()+" : " if ctr == False else "")+pwd+_prompt[os.name])
		if code == "-q":
			shutdown()

		elif code == "..":
			os.chdir("..")

		elif code == ".":
			os.chdir(".")

		elif code == "cd":
			file.cd(easygui.diropenbox("Choice directory:","cd"))

		elif "cd " in code and len(code) > 3:
			file.cd(code[3:])

		elif code == "~":
			file.cd(os.path.expanduser('~'))

		elif code == "-h":
			help()

		elif "-i" in code:
			exec("import "+code[3:])

		elif code == "-o":
			optlist = option()
			cter = optlist[0]
			User.activaty.d = optlist[1]

		else:
			try:
				exec(User.activaty.history if code == "-h" else code)
				if User.activaty == None:
					admin = User(easygui.enterbox("Input new username:","Logout"))
					main()
				User.activaty.cachefile.write("Run:\n\tCode:\n\t\t"+User.activaty.history+"\n")
				User.activaty.cachefile.flush()
			except KeyboardInterrupt:
				shutdown()
			except NameError as err:
				print("NameError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
				if User.activaty.d:
					if easygui.boolbox("If something went wrong, press <Debug> to debug","Oops!",("[D]ebug","[I]gnore")):
						while True:
							code_d = easygui.choicebox("If something went wrong","debug",("view","log","end"))
							if code_d == "view":
								exec("print({:s})".format(easygui.enterbox("view:","debug")))
							elif code_d == "log":
								User.activaty.cachefile.read()
							elif code_d == "end":
								break
				User.activaty.cachefile.write("NameError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
				User.activaty.cachefile.flush()
			except TypeError as err:
				print("TypeError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
				if User.activaty.d:
					if easygui.boolbox("If something went wrong, press <Debug> to debug","Oops!",("[D]ebug","[I]gnore")):
						while True:
							code_d = easygui.choicebox("If something went wrong","debug",("view","log","end"))
							if code_d == "view":
								exec("print({:s})".format(easygui.enterbox("view:","debug")))
							elif code_d == "log":
								User.activaty.cachefile.read()
							elif code_d == "end":
								break
				User.activaty.cachefile.write("TypeError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
				User.activaty.cachefile.flush()
			except IOError as err:
				print("IOError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
				if User.activaty.d:
					if easygui.boolbox("If something went wrong, press <Debug> to debug","Oops!",("[D]ebug","[I]gnore")):
						while True:
							code_d = easygui.choicebox("If something went wrong","debug",("view","log","end"))
							if code_d == "view":
								exec("print({:s})".format(easygui.enterbox("view:","debug")))
							elif code_d == "log":
								User.activaty.cachefile.read()
							elif code_d == "end":
								break
				User.activaty.cachefile.write("IOError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
				User.activaty.cachefile.flush()
			except KeyError as err:
				print("KeyError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
				if User.activaty.d:
					if easygui.boolbox("If something went wrong, press <Debug> to debug","Oops!",("[D]ebug","[I]gnore")):
						while True:
							code_d = easygui.choicebox("If something went wrong","debug",("view","log","end"))
							if code_d == "view":
								exec("print({:s})".format(easygui.enterbox("view:","debug")))
							elif code_d == "log":
								User.activaty.cachefile.read()
							elif code_d == "end":
								break
				User.activaty.cachefile.write("KeyError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
				User.activaty.cachefile.flush()
			except ValueError as err:
				print("ValueError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
				if User.activaty.d:
					if easygui.boolbox("If something went wrong, press <Debug> to debug","Oops!",("[D]ebug","[I]gnore")):
						while True:
							code_d = easygui.choicebox("If something went wrong","debug",("view","log","end"))
							if code_d == "view":
								exec("print({:s})".format(easygui.enterbox("view:","debug")))
							elif code_d == "log":
								User.activaty.cachefile.read()
							elif code_d == "end":
								break
				User.activaty.cachefile.write("ValueError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
				User.activaty.cachefile.flush()
			except AttributeError as err:
				print("AttributeError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
				if User.activaty.d:
					if easygui.boolbox("If something went wrong, press <Debug> to debug","Oops!",("[D]ebug","[I]gnore")):
						while True:
							code_d = easygui.choicebox("If something went wrong","debug",("view","log","end"))
							if code_d == "view":
								exec("print({:s})".format(easygui.enterbox("view:","debug")))
							elif code_d == "log":
								User.activaty.cachefile.read()
							elif code_d == "end":
								break
				User.activaty.cachefile.write("AttributeError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
				User.activaty.cachefile.flush()
				User.activaty.d = debug


def shutdown():
	if easygui.boolbox("Do you want to exit?","Exit"):
		User.activaty.logout()
		quit()
	else:
		main()


def option(debug=User.activaty.d):
	ctr = cter
	while True:
		opt = easygui.choicebox("Options: ","option",["Debug","CleanTerminal","QuitOption"])
		if opt == None:
			break
		if "Debug" in opt:
			debug = False if debug else True
		if "CleanTerminal" in opt:
			ctr = False if ctr else True
		if "QuitOption" in opt:
			break
	return [ctr,debug]
		
		


if __name__ == "__main__":
	print("Ashome V"+VERSION)
	print("Environment Version:",platform.python_version())
	main()