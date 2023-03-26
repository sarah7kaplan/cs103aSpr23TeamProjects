# Options:
# 0. quit
# 1. show categories
# 2. add category
# 3. modify category
# 4. show transactions
# 5. add transaction
# 6. delete transaction
# 7. summarize transactions by date
# 8. summarize transactions by month
# 9. summarize transactions by year
# 10. summarize transactions by category
# 11. print this menu

import sqlite3
from transaction import Transaction
filename=""
userInput=input("Please select an action:\n0. quit\n1. show categories\n2. add category\n3. modify category\n4. show transactions\n5. add transaction\n6. delete transaction\n7. summarize transactions by date\n8. summarize transactions by month\n9. summarize transactions by year\n10. summarize transactions by category\n11. print this menu\n")
if userInput==0:
    quit
if userInput==1:
    t=Transaction(filename)

def quit():

def show_categories():

def add_category():

def modify_category():

def show_transactions():

def add_transaction(self, item_number, amount, category, date, description):
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute('''INSERT INTO transactions (item_number, amount, category, date, description)
                            VALUES (?, ?, ?, ?, ?)''', (item_number, amount, category, date, description))
            conn.commit()

def delete_transaction():

def sum_date():

def sum_month():

def sum_year():

def sum_cat():

def print_menu():