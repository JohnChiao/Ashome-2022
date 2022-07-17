MODULE = "[updater]"
import os
import zipfile


def update():
	print(MODULE+"Scanning update direction...")
	if os.path.isfile("update\\UPD.zip"):
		print(MODULE+"Exists packages install?",end=" ")
		if input("(Y/N)") == "y":
			pack = zipfile.ZipFile("UPD.zip")
			print(MODULE+"Package:", pack.read("UPD.zip"))
