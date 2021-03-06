import unittest
from discount.app import (
    apply_percentage_discount,
    apply_flat_discount,
    validate_discount)


class TestDiscounts(unittest.TestCase):

    def test_apply_percentage_discount_return_cost_less_discount_of_cost(self):
        test_cases = [
            (230, 5, 219), (937, 10, 844), (767, 23, 591), (1630, 77, 375)]
        for cost, discount, expected in test_cases:
            discounted_price = apply_percentage_discount(cost, discount)
            self.assertEqual(expected, discounted_price)

    def test_apply_flat_discount_returns_cost_less_flat_discount(self):
        test_cases = [
            (230, 5, 225), (937, 10, 927), (767, 23, 744), (1630, 77, 1553)]
        for cost, discount, expected in test_cases:
            discounted_price = apply_flat_discount(cost, discount)
            self.assertEqual(expected, discounted_price)


class TestDiscountValidation(unittest.TestCase):

    def test_validate_discount_returns_None_if_prices_positive(self):
        response = validate_discount(100, 10)
        self.assertEqual(response, None)

    def test_validate_discount_raises_ValueError_if_price_negative(self):
        with self.assertRaises(ValueError) as err:
            validate_discount(0, 100)
        self.assertIsInstance(err.exception, ValueError)
