import sqlite3

class Cocktail:
    def __init__(self, conn = "drinkbase.db"):
        self.conn = sqlite3.connect(conn)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
               CREATE TABLE IF NOT EXISTS drinks (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   fortress INTEGER,
                   structure TEXT,
                   price REAL,
                   stock_quantity INTEGER DEFAULT 0
               )
           ''')

        self.cursor.execute('''
               CREATE TABLE IF NOT EXISTS cocktails (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   structure TEXT,
                   price REAL,
                   stock_quantity INTEGER DEFAULT 0
               )
           ''')

        self.cursor.execute('''
               CREATE TABLE IF NOT EXISTS sales (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   item_type TEXT, 
                   item_id INTEGER,
                   quantity INTEGER,
                   sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
               )
           ''')

        self.conn.commit()

    def add_drink(self, name, fortress, structure, price, quantity = 0):
        self.cursor.execute('''
        INSERT INTO drinks (name, fortress, structure, price, stock_quantity)
        VALUES (?, ?, ?, ?, ?)
        ''', (name, fortress, structure, price, quantity))
        self.conn.commit()


    def update_drink_stock(self, drink_id, quantity_change):
        self.cursor.execute('''
        UPDATE drinks
        SET stock_quantity = stock_quantity + ?
        WHERE id = ?
        ''', (quantity_change, drink_id))
        self.conn.commit()

    def add_cocktail(self, name, structure, price, quantity = 0):
        self.cursor.execute('''
        INSERT INTO cocktails (name, structure, price, stock_quantity)
        VALUES (?, ?, ?, ?)
        ''', (name, structure, price, quantity))
        self.conn.commit()

    def update_cocktail_stock(self, cocktail_id, quantity_change):
        self.cursor.execute('''
        UPDATE cocktails
        SET stock_quantity = stock_quantity + ?
        WHERE id = ?
        ''', (quantity_change, cocktail_id))
        self.conn.commit()

    def sell_item(self, item_type, item_id, quantity):
        if item_type == "drink":
            self.update_drink_stock(item_id, -quantity)
        elif item_type == "cocktail":
            self.update_cocktail_stock(item_id, -quantity)

        self.cursor.execute('''
        INSERT INTO sales (item_type, item_id, quantity)
        VALUES (?, ?, ?)
        ''', (item_type, item_id, quantity))
        self.conn.commit()

    def get_drinks_stock(self):
        self.cursor.execute('SELECT id, name, stock_quantity FROM drinks')
        return self.cursor.fetchall()

    def get_cocktails_stock(self):
        self.cursor.execute('SELECT id, name, stock_quantity FROM cocktails')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    db = Cocktail()

    db.add_drink("Водка", 40, "Спирт, вода", 5000, 100)
    db.add_drink("Конъяк", 40, "Виноград, спирт", 2000, 50)

    db.add_cocktail("Мохито", "Лимон, мята", 300, 30)
    db.add_cocktail("Пина колада", "Ананас, кокос", 400, 20)

    db.sell_item("drink", 1, 5)
    db.sell_item("cocktail", 1, 2)

    print("Остатки напитков:", db.get_drinks_stock())
    print("Остатки коктейлей:", db.get_cocktails_stock())

    db.close()