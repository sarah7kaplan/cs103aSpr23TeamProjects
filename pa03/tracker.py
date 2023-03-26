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

def add_transaction(self, item_number, amount, category, date, description):
        with sqlite3.connect(self.filename) as conn:
            c = conn.cursor()
            c.execute('''INSERT INTO transactions (item_number, amount, category, date, description)
                            VALUES (?, ?, ?, ?, ?)''', (item_number, amount, category, date, description))
            conn.commit()