import unittest

from aims.dvd import DigitalVideoDisc
from aims.search_by_title import search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_title_is_case_insensitive(self):
        dvds = [DigitalVideoDisc("The Lion King")]

        results = search_by_title(dvds, "lion")

        self.assertEqual([dvd.title for dvd in results], ["The Lion King"])
