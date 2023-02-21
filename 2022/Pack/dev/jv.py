import os
import easygui


class Java:
    def __init__(self):
        try:
            os.system("java --version")
            easygui.msgbox("Java is ready", "DevFly")
            self.jar = "java --jar"
        except:
            jarpath = easygui.multenterbox(
                "Enter your compiler path", "DevFly", ["Jar"])+" --jar"
            if jarpath:
                easygui.msgbox(os.system(ccpath[0] + " --version"), "DevFly")
                self.jar = jarpath[0]

    def run(self, input="", options=""):
        os.system(jarpath+" "+input+" "+options)
