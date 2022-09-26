import os


def dirinfo(dirname,prt = False):
    if prt:
        print("IsPyModule:",)
        print()
        print("IsGitRepos:",os.path.exists(dirname+"/.git"))
    return {"IsPyModule":os.path.exists(dirname+"/__init__.py"), "IsDevSpace":os.path.exists(dirname+"/.vs") or os.path.exists(dirname+"/.vscode") or os.path.exists(dirname+"/.idea"), "IsGitRepos":os.path.exists(dirname+"/.git")}

def cleanup(dirname):
    os.system("del "+dirname+"/~")

