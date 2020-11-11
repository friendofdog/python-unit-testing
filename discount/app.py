def apply_percentage_discount(c, d):
    return c - (c * d) // 100

def apply_flat_discount(c, d):
    return c - d

def validate_discount(p, f):
    if p < 1 or f < 1:
        raise ValueError(
            "These cost / discount figures result in a negative price")


if __name__ == "__main__":
    cost = int(input("Enter cost: "))
    discount = int(input("Enter discount: "))

    percentate_discounted = apply_percentage_discount(cost, discount)
    flat_discounted = apply_flat_discount(cost, discount)

    validate_discount(cost, discount)

    print("Original cost:", cost)
    print("Cost after percentage discount:", percentate_discounted)
    print("Cost after flat discount:", flat_discounted)
