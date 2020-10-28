import unittest
from discount import apply_percentage_discount


class TestDiscounts(unittest.TestCase):

    def test_apply_percentage_discount_returns_cost_less_discount(self):
        discounted = apply_percentage_discount(800, 15)
        self.assertEqual(discounted, 680)
