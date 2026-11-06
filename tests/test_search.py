import unittest

from aims.dvd import DigitalVideoDisc
from aims.search_by_title import search_by_category
from aims.search_by_title import search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_category(self):
        dvds = [
            DigitalVideoDisc("The Lion King", category="Animation"),
            DigitalVideoDisc("Star Wars", category="Science Fiction"),
            DigitalVideoDisc("Aladdin", category="Animation"),
        ]

        results = search_by_category(dvds, "animation")

        self.assertEqual(
            [dvd.title for dvd in results],
            ["The Lion King", "Aladdin"],
        )

    def test_search_by_title_is_case_insensitive(self):
        dvds = [DigitalVideoDisc("The Lion King")]

        results = search_by_title(dvds, "lion")

        self.assertEqual([dvd.title for dvd in results], ["The Lion King"])
