from calculator import calculate_discount


def test_regular_customer():
    assert calculate_discount(100, "regular") == 20


def test_member_customer():
    assert calculate_discount(100, "premium") == 30

def test_vip_customer():
    assert calculate_discount(100, "vip") == 50