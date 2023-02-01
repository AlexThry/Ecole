import sqlite3

class Database:
	def __init__(self, database):
		assert type(database) == str, "'database' doit être de type 'set'"
		self.conn = sqlite3.connect(database)
		self.curs = self.conn.cursor()

	def request(self, command):
		self.curs.execute(command)
		self.conn.commit()

	

	