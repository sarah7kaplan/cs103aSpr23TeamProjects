import pytest
import os
import sqlite3
from transaction import Transaction

# Set up a test database file
TEST_DB_FILE = 'test.db'
if os.path.exists('test.db'):
        os.remove('test.db')

# Test add_transaction method
def test_add_transaction():
    # Initialize a transaction object using the test database file
    trans = Transaction(TEST_DB_FILE)

    # Add a transaction
    trans.add_transaction(1, 50.0, 'food', '2022-04-01', 'groceries')

    # Check that the transaction was added correctly
    with sqlite3.connect(TEST_DB_FILE) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM transactions WHERE item_number = ?', (1,))
        row = c.fetchone()
        print(row)
        assert row is not None
        assert row[1] == 1
        assert row[2] == 50.0
        assert row[3] == 'food'
        assert row[4] == '2022-04-01'
        assert row[5] == 'groceries'

