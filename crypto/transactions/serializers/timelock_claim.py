from binascii import unhexlify, hexlify

from crypto.transactions.serializers.base import BaseSerializer


class TimelockClaimSerializer(BaseSerializer):
    """Serializer handling timelock claim data
    """

    def serialize(self):
        self.bytes_data += unhexlify(self.transaction['asset']['claim']['lockTransactionId'])
        unlock_secret = hexlify(self.transaction['asset']['claim']['unlockSecret'].encode())
        self.bytes_data += unhexlify(unlock_secret)

        return self.bytes_data