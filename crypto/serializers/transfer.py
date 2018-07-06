from base58 import b58decode_check

from binary.hex.writer import write_high
from binary.unsigned_integer.writer import write_bit32, write_bit64

from crypto.serializers.base import BaseSerializer


class TransferSerializer(BaseSerializer):
    """Serializer handling transfer data
    """

    def serialize(self):
        self.bytes_data += write_bit64(self.transaction['amount'])
        self.bytes_data += write_bit32(self.transaction.get('expiration', 0))
        recipient_id = b58decode_check(self.transaction['recipientId']).hex().encode()
        self.bytes_data += write_high(recipient_id)
        return self.bytes_data
