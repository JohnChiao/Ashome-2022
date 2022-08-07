from run import *
import platform
import setup
VERSION = "2022.10.5"
code = ""
cachefile = open("__pycache__/log.txt",mode='w')
cachefile.close()


def main():
	code = "Undefined"
	cachefile = open("__pycache__/log.txt",mode='a+')
	while code:
		code = input(User.activaty.name+"@"+os.getcwd()+">")
		try:
			exec(User.activaty.history if code == "-h" else code)
			User.activaty.history = User.activaty.history if code == "-h" else code
			cachefile.write("Run:\r\n\tCode:\r\n\t\t",User.activaty.history,"\r\n")
		except KeyboardInterrupt:
			shutdown()
		except NameError as err:
			print("NameError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
			cachefile.write("NameError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
		except TypeError as err:
			print("TypeError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
			cachefile.write("TypeError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
		except IOError as err:
			print("IOError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
			cachefile.write("IOError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
		except KeyError as err:
			print("KeyError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
			cachefile.write("KeyError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
		except ValueError as err:
			print("ValueError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
			cachefile.write("ValueError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
		except AttributeError as err:
			print("AttributeError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
			cachefile.write("AttributeError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")


def launch(module,code):
	try:
		exec(module.MODULE+"."+code)
		print("Run:\r\n\tCode:\r\n\t\t",code,"\r\n")
	except KeyboardInterrupt:
		shutdown()
	except NameError as err:
		print("NameError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
	except TypeError as err:
		print("TypeError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
	except IOError as err:
		print("IOError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
	except KeyError as err:
		print("KeyError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")


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