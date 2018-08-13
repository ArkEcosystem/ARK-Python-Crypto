from hashlib import sha256

from crypto.identity.keys import public_key_from_passphrase
from crypto.message import sign_message
from crypto.resources.transaction import Transaction


class BaseTransactionBuilder(object):

    def __init__(self):
        self.transaction = Transaction()
        self.transaction.type = getattr(self, 'transaction_type', None)

    def to_dict(self):
        return self.transaction.to_dict()

    def sign(self, passphrase):
        """Sign the transaction using the given passphrase

        Args:
            passphrase (str): passphrase associated with the account sending this transaction
        """
        self.transaction.senderPublicKey = public_key_from_passphrase(passphrase)
        transaction = sha256(self.transaction.to_bytes()).digest()
        message = sign_message(transaction, passphrase)
        self.transaction.signature = message['signature']

    def second_sign(self, passphrase):
        """Sign the transaction using the given second passphrase

        Args:
            passphrase (str): 2nd passphrase associated with the account sending this transaction
        """
        transaction = sha256(self.transaction.to_bytes()).digest()
        message = sign_message(transaction, passphrase)
        self.transaction.signSignature = message['signature']

    def verify(self):
        self.transaction.verify()

    def second_verify(self):
        self.transaction.second_verify()