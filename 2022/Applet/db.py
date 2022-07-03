import sqlite3

class Database(object):
	def __init__(self,name = "root.db"):
		self.connect = sqlite3.connect(name)
		self.cursor = self.connect.cursor()

class Table(Database):
	def __init__(self,name = "Table",*data):
			strdata = ", ".join(data)
			code = "CREATE TABLE "+name+"("+strdata+")"
			self.cursor.execute(code)
