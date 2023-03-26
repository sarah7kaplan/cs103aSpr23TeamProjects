import sqlite3
import os

class Transaction:
    filename=""
    def __init__(self,filename):
        self.filename = filename
        self.create_table()
    def add_transaction(self, item_number, amount, category, date, description):
        with sqlite3.connect(self.db_file) as conn:
            c = conn.cursor()
            c.execute('''INSERT INTO transactions (item_number, amount, category, date, description)
                            VALUES (?, ?, ?, ?, ?)''', (item_number, amount, category, date, description))
            conn.commit()