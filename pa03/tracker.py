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

userInput=input("0. quit\n1. show categories\n2. add category\n3. modify category\n4. show transactions\n5. add transaction\n6. delete transaction\n7. summarize transactions by date\n8. summarize transactions by month\n9. summarize transactions by year\n10. summarize transactions by category\n11. print this menu\n")
if userInput==0:
    