import os

print("Package Manager V1.0.0\nPackage list:")
path = r'./Pack'
path_list = next(os.walk(path))[1]
if os.path.exists("./Pack/__pycache"):
    path_list.remove("./Pack/__pycache")
for i in path_list:
    print(i)
name = input("Please enter the package name to import:")
if name in path_list:
    exec("from "+name+"import *")