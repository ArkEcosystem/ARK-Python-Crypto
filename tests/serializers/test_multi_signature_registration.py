from crypto.serializer import Serializer


def test_serializer(transaction_type_4):
    result = Serializer(transaction_type_4).serialize()
    assert result == transaction_type_4['serialized']
