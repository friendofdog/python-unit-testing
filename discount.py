def apply_percentage_discount(c, d):
    return c - (c * d) // 100


if __name__ == "__main__":
    cost = 100
    discount = 10
    after_discount = apply_percentage_discount(cost, discount)

    print("Original cost:", cost)
    print("Cost after percentage discount:", after_discount)
