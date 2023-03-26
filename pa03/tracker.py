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

# Define a function for each menu option
def quit_program():
    quit()

# Sarah Kaplan
def show_categories():
    print(t.show_categories())

# Sarah Kaplan
def add_category():
    category = input("Enter category: ")
    t.add_category(category)
    print("Category added successfully!")

# Sarah Kaplan
def modify_category():
    old = input("Which category do you want to modify? ")
    new = input("What should it become? ")
    t.modify_category(old, new)
    print("Category modified successfully!")

def show_transactions():
    pass

def add_transaction():
    t = Transaction(filename)
    item_number = int(input("Enter item number: "))
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    t.add_transaction(item_number, amount, category, date, description)
    print("Transaction added successfully!")

def delete_transaction():
    pass

def sum_date():
    pass

def sum_month():
    pass

def sum_year():
    pass

def sum_cat():
    pass

def print_menu():
    print("0. Quit")
    print("1. Show Categories")
    print("2. Add Category")
    print("3. Modify Category")
    print("4. Show Transactions")
    print("5. Add Transaction")
    print("6. Delete Transaction")
    print("7. Summarize Transactions by Date")
    print("8. Summarize Transactions by Month")
    print("9. Summarize Transactions by Year")
    print("10. Summarize Transactions by Category")
    print("11. Print this menu")

# Set up a test database file
TEST_DB_FILE = 'test.db'

# Get the filename for the production database
filename = input("Enter the filename for the database: ")

# Initialize a transaction object using the production database
t = Transaction(filename)

# Loop to handle user input
while True:
    print_menu()
    choice = int(input("Enter your choice: "))
    if choice == 0:
        quit_program()
    elif choice == 1:
        show_categories()
    elif choice == 2:
        add_category()
    elif choice == 3:
        modify_category()
    elif choice == 4:
        show_transactions()
    elif choice == 5:
        add_transaction()
    elif choice == 6:
        delete_transaction()
    elif choice == 7:
        sum_date()
    elif choice == 8:
        sum_month()
    elif choice == 9:
        sum_year()
    elif choice == 10:
        sum_cat()
    elif choice == 11:
        print_menu()
    else:
        print("Invalid choice. Please try again.")

