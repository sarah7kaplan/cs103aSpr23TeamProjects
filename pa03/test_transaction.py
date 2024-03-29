import pytest
import os
import sqlite3
from transaction import Transaction

# Set up a test database file
TEST_DB_FILE = 'test.db'

#Test show_transaction method
#Xinyi Shang
def test_show_transactions():
    #clear database
    if os.path.exists('test.db'):
        os.remove('test.db')
    # Initialize a transaction object using the test database file
    trans = Transaction(TEST_DB_FILE)

    # Add some transactions to the database
    trans.add_transaction(50.0, 'food', '2022-04-01', 'groceries')
    trans.add_transaction(25.0, 'clothing', '2022-04-02', 't-shirt')

# Check that show_transactions prints out the correct data
    with sqlite3.connect(TEST_DB_FILE) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM transactions')
        rows = c.fetchall()
        assert len(rows) == 2
        assert rows[0][1:] == (50.0, 'food', '2022-04-01', 'groceries')
        assert rows[1][1:] == (25.0, 'clothing', '2022-04-02', 't-shirt')

# Test add_transaction method
# Xinyi Shang
def test_add_transaction():
    #clear database
    if os.path.exists('test.db'):
        os.remove('test.db')
    # Initialize a transaction object using the test database file
    trans = Transaction(TEST_DB_FILE)

    # Add a transaction
    trans.add_transaction(50.0, 'food', '2022-04-03', 'groceries')

    # Check that the transaction was added correctly
    with sqlite3.connect(TEST_DB_FILE) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM transactions WHERE item_number = ?', (1,))
        row = c.fetchone()
        print(row)
        assert row is not None
        assert row[1] == 50.0
        assert row[2] == 'food'
        assert row[3] == '2022-04-03'
        assert row[4] == 'groceries'

# Test delete_transaction
# Sarah Kaplan
def test_delete():
    #clear database
    if os.path.exists('test.db'):
        os.remove('test.db')
    # Initialize a transaction object using the test database file
    trans = Transaction(TEST_DB_FILE)

    # Add a transaction and then delete it
    trans.add_transaction(50.0, 'food', '2022-04-01', 'groceries')
    trans.delete_transaction(1)

    # Check it was deleted
    with sqlite3.connect(TEST_DB_FILE) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM transactions WHERE item_number=(?)", (1,))
        row = c.fetchone()
        assert row is None

# Test sum_date
# James Yu
def test_sum_date():
    #clear database
    if os.path.exists('test.db'):
        os.remove('test.db')
    # Initialize a transaction object using the test database file
    trans = Transaction(TEST_DB_FILE)

    # Add a few transactions of various dates
    trans.add_transaction(50.0, 'food', '2022-10-29', 'groceries')
    trans.add_transaction(10.0, 'clothing', '2022-10-01', 'T-shirt')
    trans.add_transaction(20.0, 'video game', '2017-11-29', 'Cuphead')
    
    output=trans.sum_date(29)

    # Check if the correct 
    assert "groceries" in output
    assert "T-shirt" not in output
    assert "Cuphead" in output

# Test sum_month
# James Yu
def test_sum_month():
    #clear database
    if os.path.exists('test.db'):
        os.remove('test.db')
    # Initialize a transaction object using the test database file
    trans = Transaction(TEST_DB_FILE)

    # Add a few transactions of various dates
    trans.add_transaction(50.0, 'food', '2022-10-29', 'groceries')
    trans.add_transaction(10.0, 'clothing', '2022-10-01', 'T-shirt')
    trans.add_transaction(20.0, 'video game', '2017-11-29', 'Cuphead')
    
    output=trans.sum_month(11)

    # Check if the correct 
    assert "groceries" not in output
    assert "T-shirt" not in output
    assert "Cuphead" in output

# Test sum_year
# Michael Pyrdol
def test_sum_year():
    #clear database
    if os.path.exists('test.db'):
        os.remove('test.db')
    # Initialize a transaction object using the test database file
    trans = Transaction(TEST_DB_FILE)

    # Add a few transactions of various dates
    trans.add_transaction(50.0, 'food', '2022-04-29', 'groceries')
    trans.add_transaction(10.0, 'clothing', '2022-04-01', 'T-shirt')
    trans.add_transaction(20.0, 'video game', '2017-09-29', 'Cuphead')
    
    output=trans.sum_year(2022)

    # Check if the correct 
    assert "groceries" in output
    assert "T-shirt" in output
    assert "Cuphead" not in output

# Test sum_category
# Michael Pyrdol
def test_sum_category():
    #clear database
    if os.path.exists('test.db'):
        os.remove('test.db')
    # Initialize a transaction object using the test database file
    trans = Transaction(TEST_DB_FILE)

    # Add a few transactions of various dates
    trans.add_transaction(50.0, 'food', '2022-04-29', 'groceries')
    trans.add_transaction(10.0, 'clothing', '2022-04-01', 'T-shirt')
    trans.add_transaction(20.0, 'food', '2017-09-29', 'garlic')
    
    output=trans.sum_category("food")

    # Check if the correct 
    assert "groceries" in output
    assert "T-shirt" not in output
    assert "garlic" in output