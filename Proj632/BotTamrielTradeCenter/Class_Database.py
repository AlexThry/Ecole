import sqlite3


class Database:
	def __init__(self, database):
		self.database = database
		self.conn = sqlite3.connect(database)
		self.curs = self.conn.cursor()

	def commit(self):
		self.conn.commit()

	def get_idItem(self, name, level):
		idItem = self.curs.execute(f"SELECT idItem FROM Item WHERE name = '{name}' and level = '{level}'").fetchall()[0][0]
		return idItem

	def add_item(self, name, level, image):
		if not self.curs.execute(f"SELECT idItem FROM Item WHERE name = '{name}' and level = '{level}'").fetchall():
			self.curs.execute(f"INSERT INTO Item (name, level, image) VALUES (?, ?, ?)", (name, level, image))
			self.conn.commit()
			print("Item added")
		else:
			print(f"Item '{name}' at '{level}' already exist. Skipping")

	def add_sale(self, vendor, location, guild, price, date, idItem):
		if not self.curs.execute(f"SELECT idSale FROM Sale WHERE vendor = '{vendor}' and location = '{location}' and guild = '{guild}' and price = {price} and date = {date} and idItem = {idItem}").fetchall():
			self.curs.execute(f"INSERT INTO Sale (vendor, location, guild, price, date, idItem) VALUES (?, ?, ?, ?, ?, ?)", (vendor, location, guild, price, date, idItem))
			self.conn.commit()
			print("Sale added")
		else:
			print("Sale already exist. Skippping")


	def get_sale_info(self, item_name):
		return self.curs.execute(f"SELECT * FROM Sale WHERE idItem = (SELECT idItem FROM Item WHERE name = '{item_name}')").fetchall()





if __name__ == "__main__":
	db = Database("database.db")
	db.add_item("épée", "Level 1")
