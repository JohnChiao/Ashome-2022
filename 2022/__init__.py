from Applet import *
print("Booting programs...")
import platform
import os
import sys
import re
import setup
import getpass
import easygui
print("Initializing shell...")
# Global Define Start
VERSION = "2022.11.8"
code = ""
_prompt = {"nt" : " > ", "posix" : " $ "}
cter = False
username = getpass.getuser()
user = User(username, "root")
print("Python V"+platform.python_version())
# Global Define End
# Login



def main():
	code = "Undefined"
	global cter
	global user
	while True:
		user = User.activaty
		pwd = os.getcwd()
		prompt_info = user.name+" @ "+platform.system()+" - \n\r"
		prompt_info = "" if cter else prompt_info
		code = input(prompt_info+pwd+_prompt[os.name])
		if code == "-q":
			shutdown()

		elif code == "..":
			os.chdir("..")

		elif code == ".":
			os.chdir(".")

		elif code == "cd":
			cd(easygui.diropenbox("Choice directory:","cd"))

		elif code[:3] == "cd " and len(code) > 3:
			cd(code[3:])

		elif code == "~":
			cd(os.path.expanduser('~'))

		elif "-i" in code:
			if easygui.ccbox("Install "+code[3:]+"?", "Package Manager"):
				exec("from "+code[3:]+" import *")

		elif code == "-l":
			break

		else:
			try:
				exec(user.history if code == "-h" else code)
				if user == None:
					User(easygui.enterbox("Input new username:","Login"))
					main()

			except NameError as err:
				print("\n\r", "NameError:\n\tCode:\n\t\t",
									code, "\n\tDatail:\n\t\t", err, "\n")

			except TypeError as err:
				print("\n\r", "TypeError:\n\tCode:\n\t\t",
									code, "\n\tDatail:\n\t\t", err, "\n")

			except IOError as err:
				print("\n\r", "IOError:\n\tCode:\n\t\t",
									code, "\n\tDatail:\n\t\t", err, "\n")
				
			except KeyError as err:
				print("\n\r", "KeyError:\n\tCode:\n\t\t",
									code, "\n\tDatail:\n\t\t", err, "\n")

			except ValueError as err:
				print("\n\r", "ValueError:\n\tCode:\n\t\t",
									code, "\n\tDatail:\n\t\t", err, "\n")

			except AttributeError as err:
				print("\n\r", "AttributeError:\n\tCode:\n\t\t",
									code, "\n\tDatail:\n\t\t", err, "\n")

			except IndexError as err:
				print("\n\r", "IndexError:\n\tCode:\n\t\t",
									code, "\n\tDatail:\n\t\t", err, "\n")
			
			except:
				print("\n\r", "Error:\n\tCode:\n\t\t", code)

			else:
				print("\n\r")


def shutdown():
	if easygui.boolbox("Do you want to exit?","Exit"):
		print("Logouting user",User.activaty.name,"...")
		User.activaty.logout()
		print("Quiting terminal...")
		quit()
	else:
		main()


def start():
	while True:
		if easygui.ccbox("Welcome!","Start",["[L]ogin or Sign up","[Q]uit"]):
			ulogin = easygui.choicebox("Login","Login",USERS+["Sign Up..."])
			if ulogin == "Sign Up...":
				t = easygui.multpasswordbox("Sign up:", "Sign Up", [
											"Username", "Password"])
				if not easygui.ynbox("Sign up "+t[0]+"?", "Sign Up"):
					t = None
				if t[0]:
					User(*t)
					main()
			elif ulogin:
				try:
					passwd = easygui.passwordbox("Input password:", "Login")
					User(name=ulogin, passwd=passwd)
					main()
				except ConnectionError as err:
					easygui.msgbox(err, "Error", "Cencel")
			else:
				continue
		else:
			shutdown()


if __name__ == "__main__":
	start()

