import os
import zipfile


def update():
	print("Scanning update direction...")
	if os.path.isfile("update\\UPD.zip"):
		print("Exists packages install?",end=" ")
		if input("(Y/N)") == "y":
			pack = zipfile.ZipFile("UPD.zip")
			print("Package:", pack.read("UPD.zip"))
