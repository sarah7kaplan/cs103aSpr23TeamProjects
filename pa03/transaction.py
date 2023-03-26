import sqlite3
import os

class Transaction:
    filename=""
    def __init__(self,filename):
        self.filename = filename
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            item_number INTEGER,
                            amount REAL,
                            category TEXT,
                            date TEXT,
                            description TEXT
                        )''')
            conn.commit()
   
    def add_transaction(self, item_number, amount, category, date, description):
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute('''INSERT INTO transactions (
                            item_number, amount, category, date, description
                        ) VALUES (?, ?, ?, ?, ?)''', (item_number, amount, category, date, description))
            conn.commit()

