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
                            item_number INTEGER PRIMARY KEY,
                            amount REAL,
                            category TEXT,
                            date TEXT,
                            description TEXT
                        )''')
            conn.commit()
    
    #Xinyi Shang
    def show_transactions(self,filename):
        with sqlite3.connect(filename) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM transactions')
            rows = c.fetchall()
            if not rows:
                print("No transactions to display.")
            else:
                print("Item Number", "Amount", "Category", "Date", "Description")
                for row in rows:
                    print(row[0], row[1], row[2], row[3], row[4])

    #Xinyi Shang
    def add_transaction(self, amount, category, date, description):
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute('SELECT COUNT(*) FROM transactions')
            count = c.fetchone()[0]
            if count == 0:
                item_number = 1
            else:
                c.execute('SELECT MAX(item_number) FROM transactions')
                max_item_number = c.fetchone()[0]
                item_number = max_item_number + 1
            c.execute('''INSERT INTO transactions (
                            item_number, amount, category, date, description
                        ) VALUES (?, ?, ?, ?, ?)''', (item_number, amount, category, date, description))
            conn.commit()

   
    # Sarah Kaplan
    def delete_transaction(self, trans):
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM transactions where item_number=(?)",(trans,))
            conn.commit()

    # Michael Pyrdol
    def sum_date(self,date):
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM transactions')
            rows=c.fetchall()
            if not rows:
                print("No transactions to display.")
            else:
                date=False
                for row in rows:
                    if row[3].split("-")[2]==date:
                        date=True
                if date==True:
                    print("Item Number", "Amount", "Category", "Date", "Description")
                    for row in rows:
                        if row[3].split("-")[2]==date:
                            print(row[0], row[1], row[2], row[3], row[4])
            
    # Michael Pyrdol
    def sum_month(self,month):
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM transactions')
            rows=c.fetchall()
            if not rows:
                print("No transactions to display.")
            else:
                month=False
                for row in rows:
                    if row[3].split("-")[1]==month:
                        month=True
                if month==True:
                    print("Item Number", "Amount", "Category", "Date", "Description")
                    for row in rows:
                        if row[3].split("-")[1]==month:
                            print(row[0], row[1], row[2], row[3], row[4])
    # Michael Pyrdol
    def sum_year(self,year):
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM transactions')
            rows=c.fetchall()
            if not rows:
                return "No transactions to display."
            else:
                correctYear=False
                for row in rows:
                    if row[3].split("-")[0]==str(year):
                        correctYear=True
                if correctYear==True:
                    theString="Item Number", "Amount", "Category", "Date", "Description"
                    # print("Item Number", "Amount", "Category", "Date", "Description")
                    for row in rows:
                        if row[3].split("-")[0]==str(year):
                            theString+=row[0], row[1], row[2], row[3], row[4]
                            # print(row[0], row[1], row[2], row[3], row[4])
                    return theString