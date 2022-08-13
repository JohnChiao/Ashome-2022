from run import *
import platform
import setup
VERSION = "2022.10.5"
code = ""
ca = open("__pycache__/log.txt",mode='w')
ca.close()
del ca


def main():
	code = "Undefined"
	while code:
		code = input(User.activaty.name+"@"+os.getcwd()+">")
		try:
			exec(User.activaty.history if code == "-h" else code)
			User.activaty.history = User.activaty.history if code == "-h" else code
			User.activaty.cachefile.write("Run:\r\n\tCode:\r\n\t\t"+User.activaty.history+"\r\n")
			User.activaty.cachefile.flush()
		except KeyboardInterrupt:
			shutdown()
		except NameError as err:
			print("NameError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
			User.activaty.cachefile.write("NameError:\r\n\tCode:\r\n\t\t"+code+"\r\n\tDatail:\r\n\t\t"+err+"\r\n")
			User.activaty.cachefile.flush()
		except TypeError as err:
			print("TypeError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
			User.activaty.cachefile.write("TypeError:\r\n\tCode:\r\n\t\t"+code+"\r\n\tDatail:\r\n\t\t"+err+"\r\n")
			User.activaty.cachefile.flush()
		except IOError as err:
			print("IOError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
			User.activaty.cachefile.write("IOError:\r\n\tCode:\r\n\t\t"+code+"\r\n\tDatail:\r\n\t\t"+err+"\r\n")
			User.activaty.cachefile.flush()
		except KeyError as err:
			print("KeyError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
			User.activaty.cachefile.write("KeyError:\r\n\tCode:\r\n\t\t"+code+"\r\n\tDatail:\r\n\t\t"+err+"\r\n")
			User.activaty.cachefile.flush()
		except ValueError as err:
			print("ValueError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
			User.activaty.cachefile.write("ValueError:\r\n\tCode:\r\n\t\t"+code+"\r\n\tDatail:\r\n\t\t"+err+"\r\n")
			User.activaty.cachefile.flush()
		except AttributeError as err:
			print("AttributeError:\r\n\tCode:\r\n\t\t",code,"\r\n\tDatail:\r\n\t\t",err,"\r\n")
			User.activaty.cachefile.write("AttributeError:\r\n\tCode:\r\n\t\t"+code+"\r\n\tDatail:\r\n\t\t"+err+"\r\n")
			User.activaty.cachefile.flush()


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