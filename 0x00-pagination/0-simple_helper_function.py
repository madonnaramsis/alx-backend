#!/usr/bin/env python3
"""This module contains a simple helper function for pagination."""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing
        the start index and end index of the range.

    """
    return (page * page_size - page_size, page * page_size)
