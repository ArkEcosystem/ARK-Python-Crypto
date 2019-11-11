from crypto.constants import TRANSACTION_DELEGATE_RESIGNATION
from crypto.transactions.builder.delegate_resignation import DelegateResignation


def test_delegate_resignation_transaction():
    """Test if delegate resignation transaction gets built
    """
    transaction = DelegateResignation()
    transaction.sign('testing')
    transaction_dict = transaction.to_dict()
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_DELEGATE_RESIGNATION
    transaction.verify()  # if no exception is raised, it means the transaction is valid
