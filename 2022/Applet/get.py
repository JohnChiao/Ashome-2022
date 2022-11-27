import easygui
import webbrowser

class GetClient:
	def __init__(self):
		self.bookmarks = ["","","","","",""]
		while True:
			choice = easygui.buttonbox("Start page", "Get Browser Launcher", ["Home page", "Bookmarks", "Search...", "Open website", "Setting"])
			if choice == "Home page":
				webbrowser.open("msn.sn")
			elif choice == "Bookmarks":
				bkm = easygui.choicebox("Choice a bookmark", "Browse...", self.bookmarks)
				if bkm:
					webbrowser.open(bkm)
			elif choice == "Search...":
				egn = easygui.choicebox("Search engine:", "Browse...", ["https://www.baidu.com/s?&tn=68018901_2_oem_dgie=utf-8&wd=", "https://www.google.com/search?q=", "https://www.bing.com/search?q="])
				if egn:
					webbrowser.open(egn + easygui.enterbox("Search:", "Browse..."))
			elif choice == "Open website":
				webbrowser.open(easygui.enterbox("Browse:", "Browse..."))
			elif choice == "Setting":
				self.bookmarks = easygui.multenterbox("Set bookmarks", "Setting", ["1","2","3","4","5","6"])
			else:
				break


def get():
	client = GetClient()

