import os
import shutil


def build(name):
	print("Building applet...")
	os.rename("Pack/"+name,"app.py")
	print("Build succesful!")

def install():
	print("Installing your applet...")
	shutil.copy2("Pack/app.py","Applet/")
	print("Installation succesful!")

