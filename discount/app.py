def apply_percentage_discount(c, d):
    return c - (c * d) // 100

def apply_flat_discount(c, d):
    return c - d


if __name__ == "__main__":
    cost = int(input("Enter cost: "))
    discount = int(input("Enter discount: "))
    percentate_discounted = apply_percentage_discount(cost, discount)
    flat_discounted = apply_flat_discount(cost, discount)

    print("Original cost:", cost)
    print("Cost after percentage discount:", percentate_discounted)
    print("Cost after flat discount:", flat_discounted)
