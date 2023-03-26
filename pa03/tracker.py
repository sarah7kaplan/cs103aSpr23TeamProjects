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
import transaction

from transaction import Transaction

class Tracker:
    def __init__(self, db_filename):
        self.db = Transaction(db_filename)

    def add_transaction(self):
        item_number = int(input("Enter item number: "))
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        self.db.add_transaction(item_number, amount, category, date, description)
        print("Transaction added successfully!")
