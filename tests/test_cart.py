import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_20_dvds_succeeds_but_21st_fails(self):
        cart = Cart()

        for index in range(20):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {index}")))

        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21")))
        self.assertEqual(len(cart.items), 20)

    def test_discounted_total(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD", cost=100))

        self.assertEqual(cart.get_discounted_total(20), 80)

    def test_discount_percent_over_100_raises_value_error(self):
        cart = Cart()

        with self.assertRaises(ValueError):
            cart.get_discounted_total(150)