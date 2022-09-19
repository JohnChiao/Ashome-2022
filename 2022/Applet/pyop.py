import os


def python(name, options = "", func = ""):
	os.system("python "+options+" "+name+" "+func)


def python3(name, options = "", func = ""):
	os.system("python3 "+options+" "+name+" "+func)
