import pytest
from transaction import Transaction

@pytest.fixture
def transaction():
    return Transaction('test.db')

def test_add_transaction(transaction):
    # Add a new transaction
    transaction.add_transaction('Item 1', 10.0, 'Groceries', '2023-03-26', 'Groceries from Hannaford')
    
    # Retrieve the transaction from the database
    result = transaction.get_transactions()
    
    # Verify that the transaction was added
    assert len(result) == 1
    assert result[0]['item'] == 'Item 1'
    assert result[0]['amount'] == 10.0
    assert result[0]['category'] == 'Groceries'
    assert result[0]['date'] == '2023-03-26'
    assert result[0]['description'] == 'Groceries from Hannaford'
