# Options:
# 0. quit
# 1. show categories XXX
# 2. add category XXX
# 3. modify category XXX
# 4. show transactions
# 5. add transaction
# 6. delete transaction
# 7. summarize transactions by date
# 8. summarize transactions by month
# 9. summarize transactions by year
# 10. summarize transactions by category
# 11. print this menu

from transaction import Transaction

def quit_program():
    quit()

#Xinyi Shang
def show_transactions():
    t.show_transactions(filename)

#Xinyi Shang
def add_transaction():
    t = Transaction(filename)
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    t.add_transaction(amount, category, date, description)
    print("Transaction added successfully!")

# Sarah Kaplan
def delete_transaction():
    trans = int(input("Please enter the transaction item number you would like to delete: "))
    t.delete_transaction(trans)
    print("Transaction deleted successfully!")

# Michael Pyrdol
def sum_date():
    date=input("Please enter the desired date (DD): ")
    print(t.sum_date(date))

# Michael Pyrdol
def sum_month():
    month=input("Please enter the desired month (MM): ")
    print(t.sum_month(month))

# Michael Pyrdol
def sum_year():
    year=input("Please enter the desired year (YYYY): ")
    print(t.sum_year(year))

# Michael Pyrdol
def sum_categories():
    category=input("Please enter the desired category: ")
    print(t.sum_category(category))

def print_menu():
    print("0: Quit")
    print("1: Show Transactions")
    print("2: Add Transaction")
    print("3: Delete Transaction")
    print("4: Summarize Transactions by Date")
    print("5: Summarize Transactions by Month")
    print("6: Summarize Transactions by Year")
    print("7: Summarize Transactions by Category")
    print("8: Print this menu")

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
        show_transactions()
    elif choice == 2:
        add_transaction()
    elif choice == 3:
        delete_transaction()
    elif choice == 4:
        sum_date()
    elif choice == 5:
        sum_month()
    elif choice == 6:
        sum_year()
    elif choice == 7:
        sum_categories()
    elif choice == 8:
        print_menu()
    else:
        print("Invalid choice. Please try again.")