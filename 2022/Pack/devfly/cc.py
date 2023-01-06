import os
import easygui


class Clang:
    def __init__(self):
        try:
            easygui.msgbox(os.system("cc --version"), "DevFly")
            self.cc = "cc"
        except:
            ccpath = easygui.enterbox("Enter your compiler path")
            if ccpath:
                easygui.msgbox(os.system(ccpath + " --version"), "DevFly")
                self.cc = ccpath

    def compile(self, input="", options=""):
        os.system(self.cc + " " + input + " " + options)
        return 0

    def run(self, input="", output="./output/CC", options=""):
        os.system(self.cc + " " + input + " -o " + output + " " + options)
        os.system(output)
