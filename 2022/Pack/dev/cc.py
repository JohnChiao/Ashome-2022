import os
import easygui


class Clang:
    def __init__(self):
        try:
            os.system("cc --version")
            easygui.msgbox("Clang CC is ready", "DevFly")
            self.cc = "cc"
            self.cpp = "clang++"
        except:
            ccpath = easygui.multenterbox(
                "Enter your compiler path", "DevFly", ["C", "C++"])
            if ccpath:
                easygui.msgbox(os.system(ccpath[0] + " --version"), "DevFly")
                self.cc = ccpath[0]
                self.cpp = ccpath[1]

    def compile(self, input="", output="./CC", options=""):
        f = open(output, "w")
        f.close()
        cc = self.cpp if ".cpp" in input or ".cxx" in input else self.cc
        os.system(cc + " " + input + " -o " + output + " " + options)
        return 0

    def run(self, input="", output="./CC", options=""):
        self.compile(input, output, options)
        os.system(output)


class VC:
    def __init__(self):
        try:
            easygui.msgbox(os.system("cl --version"), "DevFly")
            self.cc = "cl"
            self.cpp = "cl"
        except:
            ccpath = easygui.multenterbox(
                "Enter your compiler path", "DevFly", ["C", "C++"])
            if ccpath:
                easygui.msgbox(os.system(ccpath[0] + " --version"), "DevFly")
                self.cc = ccpath[0]
                self.cpp = ccpath[1]

    def compile(self, input="", options=""):
        cc = self.cpp if ".cpp" in input or ".cxx" in input else self.cc
        os.system(cc + " " + input + " " + options)
        return 0

    def run(self, input="", output="./output/CC", options=""):
        cc = self.cpp if ".cpp" in input or ".cxx" in input else self.cc
        os.system(cc + " " + input + " -o " + output + " " + options)
        os.system(output)


class GCC:
    def __init__(self):
        try:
            easygui.msgbox(os.system("gcc --version"), "DevFly")
            self.cc = "gcc"
            self.cpp = "g++"
        except:
            ccpath = easygui.multenterbox(
                "Enter your compiler path", "DevFly", ["C", "C++"])
            if ccpath:
                easygui.msgbox(os.system(ccpath[0] + " --version"), "DevFly")
                self.cc = ccpath[0]
                self.cpp = ccpath[1]

    def compile(self, input="", options=""):
        cc = self.cpp if ".cpp" in input or ".cxx" in input else self.cc
        os.system(cc + " " + input + " " + options)
        return 0

    def run(self, input="", output="./output/CC", options=""):
        cc = self.cpp if ".cpp" in input or ".cxx" in input else self.cc
        os.system(cc + " " + input + " -o " + output + " " + options)
        os.system(output)
