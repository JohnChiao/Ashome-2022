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
			User.activaty.cachefile.write("Run:\n\tCode:\n\t\t"+User.activaty.history+"\n")
			User.activaty.cachefile.flush()
		except KeyboardInterrupt:
			shutdown()
		except NameError as err:
			print("NameError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
			User.activaty.cachefile.write("NameError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
			User.activaty.cachefile.flush()
		except TypeError as err:
			print("TypeError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
			User.activaty.cachefile.write("TypeError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
			User.activaty.cachefile.flush()
		except IOError as err:
			print("IOError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
			User.activaty.cachefile.write("IOError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
			User.activaty.cachefile.flush()
		except KeyError as err:
			print("KeyError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
			User.activaty.cachefile.write("KeyError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
			User.activaty.cachefile.flush()
		except ValueError as err:
			print("ValueError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
			User.activaty.cachefile.write("ValueError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
			User.activaty.cachefile.flush()
		except AttributeError as err:
			print("AttributeError:\n\tCode:\n\t\t",code,"\n\tDatail:\n\t\t",err,"\n")
			User.activaty.cachefile.write("AttributeError:\n\tCode:\n\t\t"+code+"\n\tDatail:\n\t\t"+str(err)+"\n")
			User.activaty.cachefile.flush()


def shutdown():
	if input("\nExit Ashome?(y/n)").lower() == "y":
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