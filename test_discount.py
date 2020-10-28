import unittest
from discount import apply_percentage_discount, apply_flat_discount


class TestDiscounts(unittest.TestCase):

    def test_apply_percentage_discount_return_cost_less_discount_of_cost(self):
        discounted_price = apply_percentage_discount(230, 5)
        self.assertEqual(219, discounted_price)

    def test_apply_flat_discount_returns_cost_less_flat_discount(self):
        discounted_price = apply_flat_discount(10, 5)
        self.assertEqual(5, discounted_price)
