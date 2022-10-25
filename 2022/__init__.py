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
VERSION = "2022.11"
code = ""
_ca = open("__pycache__/log.txt",mode='w')
_ca.close()
del _ca
_prompt = {"nt" : " > ", "posix" : " $ "}
cter = False
username = getpass.getuser()
ulist = ["SYSTEM",username]
# Global Define Stop
# Login



def main():
	code = "Undefined"
	global cter
	while True:
		pwd = os.getcwd()
		prompt_info = User.activaty.name+" @ "+platform.system()+" : "
		prompt_info = "" if cter else prompt_info
		code = input(prompt_info+pwd+_prompt[os.name])
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

		elif code == "-l":
			return start(User.activaty.name)

		else:
			try:
				exec(User.activaty.history if code == "-h" else code)
				if User.activaty == None:
					admin = User(easygui.enterbox("Input new username:","Login"))
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


def option():
	ctr = cter
	optl = None
	debug=User.activaty.d
	while True:
		opt = easygui.choicebox("Options: ","option",["Debug Mode: "+str(debug),"Clean Terminal: "+str(ctr),"Apply Setting","Quit Option"])
		if opt == None:
			break
		elif "Debug" in opt:
			debug = False if debug else True
		elif "Clean" in opt:
			ctr = False if ctr else True
		elif "Apply" in opt:
			optl = [ctr,debug]
		else:
			break
	return optl if optl else [cter,User.activaty.d]

def start(userlist):
	if easygui.ccbox("Welcome!","Start",["[L]ogin or Sign up","[Q]uit"]):
		ulogin = easygui.choicebox("Login","Login",userlist)
		if ulogin:
			User(name = ulogin)
			main()
	else:
		quit()


if __name__ == "__main__":
	print("Ashome V"+VERSION)
	print("Environment Version:",platform.python_version())
	start(ulist)