import os
import easygui


class Python:
    def __init__(self):
        try:
            os.system("python --version")
            easygui.msgbox("Java is ready", "DevFly")
            self.py = "python"
        except:
            pypath = easygui.multenterbox(
                "Enter your compiler path", "DevFly", ["Jar"])
            if pypath:
                easygui.msgbox(os.system(pypath[0] + " --version"), "DevFly")
                self.py = pypath[0]

    def run(self, input="", options=""):
        os.system(pypath+" "+input+" "+options)
