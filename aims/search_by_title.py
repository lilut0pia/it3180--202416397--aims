"""Utilities for searching DVDs by title and category."""


def search_by_category(dvds, category):
    """Return DVDs whose category contains ``category``.

    The search is case-insensitive and keeps the order of ``dvds``.
    An empty category returns no results.
    """
    if not category:
        return []

    query = category.casefold()
    return [dvd for dvd in dvds if query in dvd.category.casefold()]


def search_by_title(dvds, title):
    """Return DVDs whose title contains ``title``.

    The search is case-insensitive and keeps the order of ``dvds``.
    An empty title returns no results.
    """
    if not title:
        return []

    query = title.casefold()
    return [dvd for dvd in dvds if query in dvd.title.casefold()]
