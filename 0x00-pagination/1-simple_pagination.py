#!/usr/bin/env python3
'''
Module for pagination of a database of popular baby names.
'''
import csv
from typing import List
from math import ceil
from typing import Tuple


def index_range(page_number: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of the start
    and end indices for a given page number and page size.
    """
    start_index = (page_number - 1) * page_size
    end_index = page_number * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        ''' Initialize instance. '''
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(
                    self, page_number: int = 1, page_size: int = 10
                ) -> List[List]:
        '''Return a page of the dataset
        based on the given page number and page size.

        Args:
            page_number (int): The page number to retrieve. Default is 1.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            List[List]: A list of rows
            representing the requested page of the dataset.

        Raises:
            AssertionError: If page_number
            or page_size is not a positive integer.

        '''
        assert isinstance(page_number, int) and isinstance(page_size, int)
        assert page_number > 0 and page_size > 0
        indices = index_range(page_number, page_size)
        start_index = indices[0]
        end_index = indices[1]
        try:
            return self.dataset()[start_index:end_index]
        except IndexError:
            return []
