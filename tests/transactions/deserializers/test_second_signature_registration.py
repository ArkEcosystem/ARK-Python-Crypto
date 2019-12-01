from crypto.transactions.deserializer import Deserializer


def test_second_signature_registration_deserializer():
    serialized = 'ff02170100000001000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1920065cd1d000000000003699e966b2525f9088a6941d8d94f7869964a000efe65783d78ac82e1199fe60960901885e7a4915fae19bbbd4d189fb1dd199d37650dfa6d6aea4495b5d0f28c674e83c4e198a1d2e789739c5523772c5dcf27d89a281868f8757801df89d848'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 23
    assert actual.typeGroup == 1
    assert actual.type == 1
    # Should be 1, but fixture generated with the fixture generator was at 0, so as the serialized string
    assert actual.nonce == 0
    assert actual.senderPublicKey == '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'
    assert actual.fee == 500000000
    # Not sure here about the b'', is it because of the new way to sign ? Might have to check this
    assert actual.signature == b'60901885e7a4915fae19bbbd4d189fb1dd199d37650dfa6d6aea4495b5d0f28c674e83c4e198a1d2e789739c5523772c5dcf27d89a281868f8757801df89d848'
    assert actual.amount == 0
    assert actual.id == 'd1e5513ee2c13994dbd4a9fc134740b25e222d1737816c6a48a69cf6ca209a4b'
    assert actual.asset['signature']['publicKey'] == '03699e966b2525f9088a6941d8d94f7869964a000efe65783d78ac82e1199fe609'  # noqa

    # actual.verify()
