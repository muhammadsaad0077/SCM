def calculate_discount(price, memberType):
    if memberType == "regular":
        return price * 0.20
    if memberType == "premium":
        return price * 0.30

    return price * 0.10