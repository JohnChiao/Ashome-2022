from run import *
import platform
import setup
VERSION = "2022.10.3"
code = ""


def main():
	code = "Undefined"
	while code:
		code = input(User.activaty.name+"@"+os.getcwd()+">")
		try:
			exec(User.activaty.history if code == "-h" else code)
			User.activaty.history = User.activaty.history if code == "-h" else code
		except KeyboardInterrupt:
			shutdown()
		except NameError as err:
			print("NameError\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"")
		except TypeError as err:
			print("TypeError\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"")
		except IOError as err:
			print("IOError\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"")
		except KeyError as err:
			print("KeyError\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"")


def shutdown():
	if input("\r\nExit Ashome?(y/n)").lower() == "y":
		User.activaty.logout()
		quit()
	else:
		main()


if __name__ == "__main__":
	username = input("Login:")
	admin = User(name = username if username else "Admin")
	print("Ashome V"+VERSION)
	print("Environment Version:",platform.python_version())
	main()