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

    def test_sort_by_title(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("The Lion King"))
        cart.add_dvd(DigitalVideoDisc("Aladdin"))
        cart.add_dvd(DigitalVideoDisc("Star Wars"))

        cart.sort_by_title()

        self.assertEqual(
            [dvd.title for dvd in cart.items],
            ["Aladdin", "Star Wars", "The Lion King"],
        )

    def test_sort_by_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Expensive", cost=30))
        cart.add_dvd(DigitalVideoDisc("Cheap", cost=10))
        cart.add_dvd(DigitalVideoDisc("Moderate", cost=20))

        cart.sort_by_cost()

        self.assertEqual(
            [dvd.cost for dvd in cart.items],
            [10, 20, 30],
        )