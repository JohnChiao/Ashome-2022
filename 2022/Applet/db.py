MODULE = "db"

import sqlite3

class Database(object):
	def __init__(self,name = "root.db"):
		self.connect = sqlite3.connect(name)
		self.cursor = self.connect.cursor()

	def run(self,code = ""):
		self.cursor.execute(code)

	def close(self):
		self.cursor.close()
		self.connect.close()

	def commit(self):
		self.connect.commit()

	def relog(self):
		self.connect.rollback()

	