MODULE = "db"

import sqlite3

class Database(object):
	def __init__(self,name = "root.db"):
		self.connect = sqlite3.connect(name)
		self.cur = self.connect.cursor()

	def run(self,code = ""):
		self.cur.execute(code)

	def close(self):
		self.cur.close()
		self.connect.close()

	def commit(self):
		self.connect.commit()

	def relog(self):
		self.connect.rollback()

	