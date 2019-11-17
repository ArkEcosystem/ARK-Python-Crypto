from crypto.constants import TRANSACTION_MULTI_PAYMENT, TRANSACTION_TYPE_GROUP
from crypto.transactions.builder.base import BaseTransactionBuilder


class MultiPayment(BaseTransactionBuilder):

    transaction_type = TRANSACTION_MULTI_PAYMENT

    def __init__(self, fee=None):
        """Create a multi payment transaction

        Args:
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.typeGroup = self.get_type_group()

        if fee:
            self.transaction.fee = fee

        self.transaction.asset['payments'] = []

    def get_type_group(self):
        return TRANSACTION_TYPE_GROUP.CORE.value

    def add_payment(self, amount, recipient_id):
        self.transaction.asset['payments'].append({'amount': amount, 'recipientId': recipient_id})
