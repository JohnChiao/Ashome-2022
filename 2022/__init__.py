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
VERSION = "2022.11.5"
code = ""
_prompt = {"nt" : " > ", "posix" : " $ "}
cter = False
username = getpass.getuser()
ulist = [username]
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

		elif "-i" in code:
			exec("import "+code[3:])

		elif code == "-l":
			return start()

		else:
			try:
				exec(User.activaty.history if code == "-h" else code)
				if User.activaty == None:
					admin = User(easygui.enterbox("Input new username:","Login"))
					main()

			except KeyboardInterrupt:
				shutdown()

			except NameError as err:
				print("NameError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")

			except TypeError as err:
				print("TypeError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")

			except IOError as err:
				print("IOError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
				
			except KeyError as err:
				print("KeyError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")

			except ValueError as err:
				print("ValueError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")

			except AttributeError as err:
				print("AttributeError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")

def shutdown():
	if easygui.boolbox("Do you want to exit?","Exit"):
		User.activaty.logout()
		quit()
	else:
		main()


def start():
	global ulist
	while True:
		if easygui.ccbox("Welcome!","Start",["[L]ogin or Sign up","[Q]uit"]):
			ulogin = easygui.choicebox("Login","Login",ulist+["Sign Up..."])
			if ulogin == "Sign Up...":
				t = easygui.enterbox("Input User Name:","Sign Up")
				ulist.append(t if t else "Guest")
				User(name = t)
				main()
			elif ulogin:
				User(name = ulogin)
				main()
			else:
				continue
		else:
			quit()


if __name__ == "__main__":
	print("Ashome V"+VERSION)
	print("Environment Version:",platform.python_version())
	start()