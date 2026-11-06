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