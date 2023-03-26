import pytest
import sqlite3
from transaction import Transaction

@pytest.fixture
def transaction():
    return Transaction('test.db')

def test_add_transaction(transaction):
    transaction.add_transaction(1, 10.0, "Food", "2022-04-01", "Lunch")

    with sqlite3.connect("test.db") as conn:
        c = conn.cursor()
        c.execute('''SELECT * FROM transactions WHERE item_number = ?''', (1,))
        result = c.fetchone()
        assert result is not None
        assert result[1] == 1
        assert result[2] == 10.0
        assert result[3] == "Food"
        assert result[4] == "2022-04-01"
        assert result[5] == "Lunch"
