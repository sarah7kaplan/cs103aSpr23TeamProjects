This app uses SQL commands to examine financial transactions in a database. The user is able to use this app to examine the data.
There are also testing files to make sure that this app works.

Running pylint:
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

Running pytest:

============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-7.2.2, pluggy-1.0.0
rootdir: /Users/JamesYu/Desktop/cs103aSpr23TeamProjects-1
plugins: anyio-3.6.2
collected 6 items

pa03/test_transaction.py .(1, 50.0, 'food', '2022-04-03', 'groceries')
5
.
2

- generated xml file: /var/folders/b5/1cx4t_ss60l24pgcd18zt1880000gn/T/tmp-56498SfDaY2Xdsbu7.xml -
============================== 6 passed in 0.08s ===============================

Running tracker.py:

Enter the filename for the database: test.db
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
Enter your choice: 1
No transactions to display.
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
Enter your choice: 2
Enter amount: 50
Enter category: food
Enter date (YYYY-MM-DD): 2022-04-29
Enter description: groceries
Transaction added successfully!
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
Enter your choice: 2
Enter amount: 10
Enter category: clothing
Enter date (YYYY-MM-DD): 2022-04-01
Enter description: T-shirt
Transaction added successfully!
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
Enter your choice: 2
Enter amount: 20
Enter category: food
Enter date (YYYY-MM-DD): 2017-09-29
Enter description: garlic
Transaction added successfully!
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
Enter your choice: 1
Item Number Amount Category Date Description
1 50.0 food 2022-04-29 groceries
2 10.0 clothing 2022-04-01 T-shirt
3 20.0 food 2017-09-29 garlic
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
Enter your choice: 3
Please enter the transaction item number you would like to delete: 2
Transaction deleted successfully!
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
Enter your choice: 1
Item Number Amount Category Date Description
1 50.0 food 2022-04-29 groceries
3 20.0 food 2017-09-29 garlic
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
Enter your choice: 2
Enter amount: 10
Enter category: clothing
Enter date (YYYY-MM-DD): 2022-04-01
Enter description: T-shirt
Transaction added successfully!
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
Enter your choice: 4
Please enter the desired date (DD): 29
('Item Number', 'Amount', 'Category', 'Date', 'Description', '\n', 1, 50.0, 'food', '2022-04-29', 'groceries', '\n', 3, 20.0, 'food', '2017-09-29', 'garlic', '\n')
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
Enter your choice: 5
Please enter the desired month (MM): 04
('Item Number', 'Amount', 'Category', 'Date', 'Description', '\n', 1, 50.0, 'food', '2022-04-29', 'groceries', '\n', 4, 10.0, 'clothing', '2022-04-01', 'T-shirt', '\n')
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
Enter your choice: 6
Please enter the desired year (YYYY): 2022
('Item Number', 'Amount', 'Category', 'Date', 'Description', '\n', 1, 50.0, 'food', '2022-04-29', 'groceries', '\n', 4, 10.0, 'clothing', '2022-04-01', 'T-shirt', '\n')
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
Enter your choice: 7
Please enter the desired category: food
('Item Number', 'Amount', 'Category', 'Date', 'Description', '\n', 1, 50.0, 'food', '2022-04-29', 'groceries', '\n', 3, 20.0, 'food', '2017-09-29', 'garlic', '\n')
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
Enter your choice: 8
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
0: Quit
1: Show Transactions
2: Add Transaction
3: Delete Transaction
4: Summarize Transactions by Date
5: Summarize Transactions by Month
6: Summarize Transactions by Year
7: Summarize Transactions by Category
8: Print this menu
Enter your choice: 0
