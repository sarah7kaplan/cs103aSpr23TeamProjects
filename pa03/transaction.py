import sqlite3
import os

class Transaction:
    filename=""
    def __init__(self,filename):
        self.filename = filename
        self.create_table()
        self.item_number = 1

    def create_table(self):
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            item_number INTEGER PRIMARY KEY,
                            amount REAL,
                            category TEXT,
                            date TEXT,
                            description TEXT
                        )''')
            conn.commit()
    
    #Xinyi Shang
    def show_transactions(self):
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM transactions')
            rows = c.fetchall()
            if not rows:
                print("No transactions to display.")
            else:
                print("ID", "Item Number", "Amount", "Category", "Date", "Description")
                for row in rows:
                    print(row[0], row[1], row[2], row[3], row[4], row[5])

    #Xinyi Shang
    def add_transaction(self, amount, category, date, description):
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute('''INSERT INTO transactions (
                            amount, category, date, description
                        ) VALUES (?, ?, ?, ?)''', (amount, category, date, description))
            conn.commit()

   
    # Sarah Kaplan
    def delete_transaction(self, trans):
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM transactions where item_number=(?)",(trans))
            conn.commit()
