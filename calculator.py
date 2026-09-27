"""Simple discount calculator program."""
def calculate_discount(price, member_type):
    """Simple discount calculator program."""
    if member_type == "regular":
        return price * 0.20
    if member_type == "premium":
        return price * 0.30

    if member_type == "vip":
        return price * 0.50

    return price * 0.10
